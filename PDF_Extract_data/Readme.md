# PDF Invoice Extractor

This script extracts key details from the first page of PDF invoices, such as the invoice number, order number, invoice date, due date, total due, subtotal, and tax amount. The extracted data is then organized into a pandas DataFrame for easy manipulation and analysis.

## Features

- **PDF Parsing**: Reads the first page of each PDF invoice in the current directory.
- **Data Extraction**: Uses regular expressions to extract specific information from the PDF text.
- **Data Organization**: Converts the extracted information into a pandas DataFrame for further analysis.

## Installation

Before running the script, ensure you have the following packages installed:

```bash
pip install pypdf2 pandas
```

## Usage
1. **Save your invoices as PDFs**: Place all the PDF files you want to extract information from in the same directory as the script.

2. **Run the script**: Execute the script using Python. It will automatically detect all PDFs in the current directory, extract relevant information, and output it as a pandas DataFrame.

```bash
python main.py
```

3. **View the results**: The script will print the DataFrame with the extracted invoice details. You can further manipulate, save, or analyze this data as needed.

## Contact
For any inquiries or issues, please contact [harshanannapaneni10@gmail.com](mailto:harshanannapaneni10@gmail.com)