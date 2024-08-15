from dash import Dash, dcc, html, dash_table, Input, Output
import plotly.graph_objs as go
import pandas as pd
import yfinance as yf
import dash_bootstrap_components as dbc

class StockDashBoard:
    def __init__(self) -> None:
        # Initialise portfolio data
        self.portfolio = pd.DataFrame({
                    'Ticker': ['GOOG', 'AAPL', 'MSFT'],
                    'Shares': [10, 15, 20],
                    'Purchase_Price': [150, 200, 300],  # High purchase prices to ensure positive profit
                    'Purchase_Date': ['2023-01-15', '2023-02-10', '2023-03-05']
       })

        # Fetch stock data for each ticker:
        self.tickers = self.portfolio['Ticker'].unique()
        self.stock_data = {}
        self.portfolio['Sector'] = None
        
        for ticker in self.tickers:
            ticker_obj = yf.Ticker(ticker)
            self.stock_data[ticker] = ticker_obj.history(period="1y")
            # Get sector information
            sector = ticker_obj.info.get('sector', 'Unknown')  # Fetch the sector with a fallback to 'Unknown'
            self.portfolio.loc[self.portfolio['Ticker'] == ticker, 'Sector'] = sector


        # Calculate current portfolio values and other metrics:
        self.calculate_portfolio_metrics()

        # Initialise dash app
        self.app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
        self.setup_layout()
        self.setup_callbacks()

    def calculate_portfolio_metrics(self):
        """Calculate the necessary metrics for the portfolio"""
        self.portfolio['Current_Price']=self.portfolio['Ticker'].apply(
            lambda x:self.stock_data[x]['Close'].iloc[-1]
        )
        self.portfolio['Current_Value']=self.portfolio['Shares']*self.portfolio['Current_Price']
        self.portfolio['Total_Investment']=self.portfolio['Shares']*self.portfolio['Purchase_Price']
        self.portfolio['Profit/Loss']=self.portfolio['Current_Value'] - self.portfolio['Total_Investment']


    def generate_cummilative_return_graph(self):
        """Generate a cummilative return graph for the portfolio."""
        fig = go.Figure()
        for ticker in self.tickers:
            fig.add_trace(go.Scatter(
                x=self.stock_data[ticker].index,
                y=(self.stock_data[ticker]['Close']/self.stock_data[ticker]["Close"].iloc[0] - 1), # (present-first)/first = present/first - 1 (if present>first ==> +ve ==> Profit else Loss)
                mode='lines',
                name=f"{ticker} Cummilative Return"
            ))
        fig.update_layout(
            title='Cumulative Return Over Time',
            xaxis_title='Date',
            yaxis_title='Cummilative Return',
            template='plotly_dark'
        )
        return fig

    def generate_rsi_graph(self,ticker):
        rsi = self.calculate_rsi(self.stock_data[ticker])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.stock_data[ticker].index,
                                 y=rsi,mode='lines',
                                 name=f"{ticker} RSI"))
        fig.update_layout(title=f'{ticker} Relative Strength Index (RSI)',
                          xaxis_title='Date',yaxis_title='RSI',
                          template='plotly_dark'
                          )
        return fig

    def calculate_rsi(self,data, window=14):
        """Calculate the RSI for a given stock data."""
        delta = data['Close'].diff(1)
        gain = (delta.where(delta>0,0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain/loss
        rsi = 100 - (100/(1 + rs))
        return rsi

    def generate_moving_averages_graph(self,ticker):
        """Generate a graph with Moving Averages for a given ticker."""
        stock = self.stock_data[ticker]
        stock['SMA_50'] = stock['Close'].rolling(window=50).mean()
        stock['EMA_20'] = stock['Close'].ewm(span=20, adjust=False).mean()

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=stock.index, y=stock['Close'], mode='lines', name='Close Price'))
        fig.add_trace(go.Scatter(x=stock.index, y=stock['SMA_50'], mode='lines', name='50-Day SMA'))
        fig.add_trace(go.Scatter(x=stock.index, y=stock['EMA_20'], mode='lines', name='20-Day EMA'))
        fig.update_layout(title=f'{ticker} Moving Averages',
                          xaxis_title='Date', yaxis_title='Price (USD)',
            template='plotly_dark'
                          )
        return fig

    def generate_bollinger_bands_graph(self,ticker):
        """Generate a Bollinger Bands graph for a given ticker."""
        stock = self.stock_data[ticker]
        stock['SMA_20'] = stock['Close'].rolling(window=20).mean()
        stock['Upper_Band'] = stock['SMA_20'] + (stock['Close'].rolling(window=20).std() * 2)
        stock['Lower_Band'] = stock['SMA_20'] - (stock['Close'].rolling(window=20).std() * 2)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=stock.index, y=stock['Close'], mode='lines', name='Close Price'))
        fig.add_trace(go.Scatter(x=stock.index, y=stock['Upper_Band'], mode='lines', name='Upper Band'))
        fig.add_trace(go.Scatter(x=stock.index, y=stock['Lower_Band'], mode='lines', name='Lower Band'))
        fig.update_layout(title=f'{ticker} Bollinger Bands',
                          xaxis_title='Date', yaxis_title='Price (USD)',
            template='plotly_dark'
                          )
        return fig

    def generate_correlation_heatmap(self):
        """Generate a heatmap of correlations between different stocks in the portfolio."""
        returns = pd.DataFrame({ticker: self.stock_data[ticker]['Close'].pct_change() for ticker in self.tickers}).dropna()
        correlation = returns.corr()

        fig = go.Figure(data=go.Heatmap(
            z=correlation.values,
            x=correlation.index.values,
            y=correlation.columns.values,
            colorscale='Viridis'))
        fig.update_layout(title='Correlation Matrix of Stock Returns',
            template='plotly_dark')
        return fig

    def generate_sector_allocation_pie(self):
        """Generate a pie chart showing sector allocation of the portfolio."""
        sector_allocation = self.portfolio.groupby('Sector')['Current_Value'].sum()

        fig = go.Figure(data=[go.Pie(labels=sector_allocation.index, values=sector_allocation.values)])
        fig.update_layout(title='Sector Allocation',
                            template='plotly_dark',  # Use a dark theme for the plot

                           # Set text colors
                            title_font=dict(color='lightblue'),  # Title text color
                            font=dict(color='white'),  # General font color
                            legend=dict(font=dict(color='white')),  # Legend text color
                          )
        return fig

    def format_profit_loss(self, amount):
        """Return a formatted string with color and arrow based on profit or loss."""
        if amount > 0:
            return html.Span(f"↑ ${amount:,.2f}", style={'color': 'limegreen'})
        elif amount < 0:
            return html.Span(f"↓ ${amount:,.2f}", style={'color': 'red'})
        else:
            return html.Span(f"${amount:,.2f}", style={'color': 'white'})


    def setup_layout(self):
        """Setup the layout of the Dash app."""
        # Calculate totals for the portfolio
        total_profit_loss = self.portfolio['Profit/Loss'].sum()
        self.app.layout = dbc.Container([
            dbc.Row([
                dbc.Col(html.H1("Stock Portfolio Dashboard", className="text-center mb-4"),style={'color': '#a3d9ff'}, width=12),
            ]),

            # Portfolio Summary
            dbc.Row([
                dbc.Col([
                    html.H2("Portfolio Overview", style={'color': '#a3d9ff'}),
                    html.P(f"Total Investment: ${self.portfolio['Total_Investment'].sum():,.2f}", style={'color': '#a3d9ff'}),
                    html.P(f"Current Value: ${self.portfolio['Current_Value'].sum():,.2f}", style={'color': '#a3d9ff'}),
                     html.P([
                                html.Span("Total Profit/Loss: ", ),
                                self.format_profit_loss(total_profit_loss)],style={'color': '#a3d9ff'}),
                    # html.P(f"Total Profit/Loss: ${self.portfolio['Profit/Loss'].sum():,.2f}", style={'color': '#a3d9ff'}),

                ], width=12),
            ]),

            # Dropdown to select individual stock
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='stock-dropdown',
                        options=[{'label': ticker, 'value': ticker} for ticker in self.tickers],
                        value=self.tickers[0],  # Default value
                        style={'width': '100%', 'color': '#000'},
                        className="mb-4"
                    ),
                ], width=6),
            ]),

            # Graphs for selected stock
            dbc.Row([
                dbc.Col(dcc.Graph(id='cumulative-return-graph', figure=self.generate_cummilative_return_graph()), width=12),
            ]),

            dbc.Row([
                dbc.Col(dcc.Graph(id='rsi-graph'), width=12),
            ]),

            dbc.Row([
                dbc.Col(dcc.Graph(id='moving-averages-graph'), width=12),
            ]),

            dbc.Row([
                dbc.Col(dcc.Graph(id='bollinger-bands-graph'), width=12),
            ]),

            # Portfolio Holdings and Sector Allocation
            dbc.Row([
                dbc.Col(dcc.Graph(id='holdings-graph', figure=self.generate_sector_allocation_pie()), width=6),
                dbc.Col(dcc.Graph(id='correlation-heatmap', figure=self.generate_correlation_heatmap()), width=6),
            ]),

            # Transaction Table
            dbc.Row([
                dbc.Col([
                    dash_table.DataTable(
                        id='portfolio-table',
                        columns=[{"name": i, "id": i} for i in self.portfolio.columns],
                        data=self.portfolio.to_dict('records'),
                        style_table={'height': '300px', 'overflowY': 'auto', 'backgroundColor': '#222', 'color': '#fff'},
                        style_cell={'backgroundColor': '#333', 'color': '#fff'},
                        style_header={'backgroundColor': '#444', 'color': '#fff'},
                    ),
                ], width=12),
            ])
        ], fluid=True)


    def setup_callbacks(self):
        """Setup the callbacks to update graphs based on dropdown selection."""
        @self.app.callback(
            [Output('rsi-graph', 'figure'),
             Output('moving-averages-graph', 'figure'),
             Output('bollinger-bands-graph', 'figure')],
            [Input('stock-dropdown', 'value')]
        )
        def update_graphs(selected_ticker):
            return (self.generate_rsi_graph(selected_ticker),
                    self.generate_moving_averages_graph(selected_ticker),
                    self.generate_bollinger_bands_graph(selected_ticker))

    def run(self):
        self.app.run_server(debug=True)

if __name__== "__main__":
    dashboard = StockDashBoard()
    dashboard.run()