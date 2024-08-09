from pypdf import PdfReader
import re
import pandas as pd

# Extract data in page - 1 of invoice.
def extract_pdf(file)->str:
    # Reader object
    reader = PdfReader(file)
    page = reader.pages[0]
    text = page.extract_text()
    return text

def extract_invoice_details(text)->dict:
    # Extract important info using regex.
    invoice_number = re.search(r"Invoice Number (\S+)",text)
    order_number = re.search(r"Order Number (\S+)",text)
    invoice_date = re.search(r"Invoice Date (\w+\s\d{1,2},\s\d{4})",text)
    due_date = re.search(r"Due Date ([\w\s,]+)\n",text)
    total_due = re.search(r"Total Due \$(\S+)", text)
    sub_total = re.search(r"Sub Total \$(\S+)", text)
    tax = re.search(r"Tax \$(\S+)", text)

    # Build a dictionary of extracted info
    invoice_details = {
        "Invoice Number": invoice_number.group(1) if invoice_number else None,
        "Order Number": order_number.group(1) if order_number else None,
        "Invoice Date": invoice_date.group(1) if invoice_date else None,
        "Due Date": due_date.group(1) if due_date else None,
        "Total Due": total_due.group(1) if total_due else None,
        "Sub Total": sub_total.group(1) if sub_total else None,
        "Tax": tax.group(1) if tax else None
    }

    return invoice_details


