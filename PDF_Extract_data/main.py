import pdf_extract
import pandas as pd
import os

ls = os.listdir(os.getcwd())
pdfs = [file for file in ls if file.endswith(".pdf")]
all_invoices = []

for file in pdfs:
    text = pdf_extract.extract_pdf(file)
    # Fetch the invoice details:
    invoice_details = pdf_extract.extract_invoice_details(text)
    # Convert the details to a dataframe
    all_invoices.append(invoice_details)
    
df = pd.DataFrame(all_invoices)
print(df.head())