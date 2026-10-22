from pypdf import PdfReader

pdf_path = input("Enter the PDF file path: ")

try:
    reader = PdfReader(pdf_path)

    print("Total pages:", len(reader.pages))

    for i, page in enumerate(reader.pages, start=1):
        print(f"\n--- Page {i} ---")
        print(page.extract_text() or "No extractable text found.")

except FileNotFoundError:
    print("Error: PDF file not found. Check the file path.")

except Exception as e:
    print("Error:", e)