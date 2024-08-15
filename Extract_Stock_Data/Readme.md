# Stock Portfolio Dashboard

## Overview

The **Stock Portfolio Dashboard** is a web application built using Dash, Plotly, and other Python libraries. It provides a comprehensive view of a stock portfolio, including real-time data visualizations and portfolio metrics. Key features include:

- Cumulative return graph for the entire portfolio.
- Relative Strength Index (RSI) graph for individual stocks.
- Moving Averages graph for individual stocks.
- Bollinger Bands graph for individual stocks.
- Correlation heatmap of stock returns.
- Sector allocation pie chart of the portfolio.
- Interactive table displaying portfolio holdings.

## Features

- **Cumulative Return Graph**: Visualizes the cumulative return over time for all stocks in the portfolio.
- **RSI Graph**: Displays the Relative Strength Index for the selected stock.
- **Moving Averages Graph**: Shows both Simple Moving Average (SMA) and Exponential Moving Average (EMA) for the selected stock.
- **Bollinger Bands Graph**: Illustrates Bollinger Bands for the selected stock.
- **Correlation Heatmap**: Shows the correlation between different stocks in the portfolio.
- **Sector Allocation Pie Chart**: Represents the distribution of investments across different sectors.
- **Portfolio Table**: Lists the portfolio holdings along with key metrics like current price, total investment, and profit/loss.

## Requirements

- Python 3.8+
- Dash
- Plotly
- Pandas
- yFinance
- Dash Bootstrap Components

You can install the required packages using pip:

```bash
pip install dash plotly pandas yfinance dash-bootstrap-components
```

## Setup
1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/stock-portfolio-dashboard.git
cd stock-portfolio-dashboard
```
2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
3. **Run the Application**:

```bash
python app.py
```
The application will start a local server. Open your web browser and go to http://127.0.0.1:8050/ to view the dashboard.

## Usage
1. Portfolio Overview: See a summary of your investments, including total investment, current value, and total profit/loss.

2. Stock Selection: Use the dropdown menu to select an individual stock and view its RSI, moving averages, and Bollinger Bands.

3. Graphs and Charts: Interact with various graphs to analyze the performance and characteristics of your portfolio and individual stocks.

4. Sector Allocation: View a pie chart showing how your investments are distributed across different sectors.

5. Correlation Heatmap: Analyze the correlation between different stocks in your portfolio.

6. Transaction Table: Review the details of your portfolio holdings in a sortable and filterable table.

## Customization
You can customize the portfolio data by modifying the `self.portfolio` DataFrame in the `StockDashBoard` class in `app.py`. Adjust the tickers, shares, purchase prices, and purchase dates as needed.