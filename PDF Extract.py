import sys
import subprocess

# Install PyMuPDF package if not already installed
try:
    import fitz
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "PyMuPDF"])

import os

# Function to check if the uploaded file has a PDF extension
def is_pdf(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() == '.pdf'

# Function to upload PDF file
def upload_file():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()  # Hide the main window
    filename = askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return filename

# Upload the file
print("Please select the PDF file you want to process.")
pdf_file_path = upload_file()

# Check if the uploaded file is a PDF
if not pdf_file_path or not is_pdf(pdf_file_path):
    print("Uploaded file is either empty or not a PDF. Please select a valid PDF file.")
else:
    # Extract text from the PDF
    doc = fitz.open(pdf_file_path)
    extracted_text = ""
    for page in doc:
        extracted_text += page.get_text("text")

    # Save the extracted text to a text file
    text_file_path = 'extracted_text.txt'
    with open(text_file_path, 'w') as text_file:
        text_file.write(extracted_text)

    print(f"Text extracted and saved to {text_file_path}")
