import PyPDF2
import os

pdf_folder = "pdf"
merger = PyPDF2.PdfMerger()

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        file_path = os.path.join(pdf_folder, file)
        merger.append(file_path)

# Move the write and close outside the loop
merger.write(os.path.join(pdf_folder, "merged.pdf"))
merger.close()