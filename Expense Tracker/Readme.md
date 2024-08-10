# Expense Tracker

A basic Python script to log, view, and analyze your expenses. This tool stores expenses in a CSV file, providing simple functionalities for adding expenses, viewing all expenses, and summarizing expenses by category.

## Features

- **Add Expense**: Log your expenses by specifying the category, description, and amount.
- **View Expenses**: Display all logged expenses in a tabular format.
- **View Summary**: Get a quick overview of your expenses categorized and summed.
- **User-Friendly Menu**: A simple text-based interface to interact with the tracker.

## Requirements

- Python 3.x
- `pandas` library

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/expense-tracker.git
    cd expense-tracker
    ```

2. **Install Required Libraries**

    Use pip to install the necessary Python packages:

    ```bash
    pip install pandas
    ```

## Usage

1. **Run the Script**

    ```bash
    python main.py
    ```

2. **Follow the Menu Instructions**

    - **Add Expense**: Enter the category (e.g., Food, Transport), description, and amount.
    - **View Expenses**: Display all your logged expenses in a table.
    - **View Summary**: Get a summary of expenses categorized and summed.
    - **Exit**: Stop the script.

## Code Explanation

### File Handling

- The script checks if an `expenses.csv` file exists. If not, it creates one with headers (`Date`, `Category`, `Description`, `Amount`).

### Adding Expenses

- The `add_expense()` function logs a new expense by appending the category, description, amount, and current date/time to the CSV file.

### Viewing Expenses

- The `view_expenses()` function reads the CSV file into a `pandas` DataFrame and displays all logged expenses.

### Viewing Summary

- The `view_summary()` function groups the expenses by category and sums the amounts, providing an overview of spending by category.

### User Menu

- The script provides a simple menu-driven interface, allowing users to choose actions such as adding expenses, viewing all expenses, viewing summaries, or exiting the program.

## Future Enhancements

This basic expense tracker can be expanded with additional features:

- **Edit or Delete Expenses**: Modify or remove entries.
- **Visualizations**: Display graphs for better insights.
- **Exporting**: Export summaries to formats like Excel or PDF.
- **Google Drive Integration**: Automatically upload the CSV file to Google Drive.
- **Add More Columns/Attributes to the CSV**: Include additional attributes such as payment method, location, expense type(fixed/variable), recurring expense(monthly subscription or not) etc.
  
## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.