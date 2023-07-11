# -*- coding: utf-8 -*-
"""multiple_pdf to text.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13EtjfGdm8Mg7ZyRJT9_GcHggy2SG43mr
"""

pip install PYPDF2

import PyPDF2
from PyPDF2 import PdfReader

def convert_pdf_to_text(pdf_files, output_file):
    text = ""
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()

    with open(output_file, 'w') as file:
        file.write(text)

# Usage example
def main():
    num_files = int(input("Enter the number of PDF files: "))
    pdf_files = []
    for i in range(num_files):
        file_name = input(f"Enter the name of PDF file {i+1}: ")
        pdf_files.append(file_name)

    output_file = input("Enter the name of the output text file: ")

    convert_pdf_to_text(pdf_files, output_file)
    print("PDF to text conversion completed!")

if __name__ == '__main__':
    main()



