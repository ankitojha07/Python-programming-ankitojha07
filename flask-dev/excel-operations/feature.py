import os
from PyPDF2 import PdfReader
import pandas as pd


# Recursive function to iterate through all files and subfolders
def read_pdf_files(folder_path):
    data = []  # List to store the data

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".pdf"):
                # Open the PDF file
                filepath = os.path.join(root, filename)
                with open(filepath, "rb") as f:
                    # Read the PDF file
                    pdf = PdfReader(f)
                    # Get the number of pages in the PDF file
                    num_pages = len(pdf.pages)
                    # Get the folder name from the root path
                    folder_name = os.path.basename(root)
                    # Append the folder name, filename, and number of pages to the data list
                    data.append((folder_name, filename, num_pages))

    # Create a DataFrame from the data list
    df = pd.DataFrame(data, columns=['Folder Name', 'File Name', 'Page Number'])

    # Save the DataFrame to an Excel file

    new_directory_name = "results"
    new_directory_path = os.path.join(folder_path, new_directory_name)
    if not os.path.exists(new_directory_path):
        # Create the new directory
        os.makedirs(new_directory_path)
    else:
        print(f"Directory '{new_directory_name}' already exists.")

    output_path = r'output.xlsx'
    output_file =os.path.join(new_directory_path, output_path)

    df.to_excel(output_file, index=False)

    return output_file