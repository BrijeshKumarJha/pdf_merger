from pathlib import Path
from pypdf import PdfWriter

def pdf_merger():
    folder_input = input("Enter the name of folder: ")
    folder_path = Path(folder_input)

    pdf_files = list(folder_path.glob("*.pdf"))

    if not pdf_files:
        print("No pdf files ")
    else:
        pdf_files.sort()
        merger = PdfWriter()
        print(f"found {len(pdf_files)} pdf documents. ")
        for item in pdf_files:
            print(f" Adding {item.name}")
            merger.append(item)
            # print()
        file_name = input("Enter desired final pdf file name: ")
        if not file_name.endswith(".pdf"):
            file_name += ".pdf"
        output_path = folder_path / file_name

        merger.write(output_path)
        merger.close()
    print(f"Succesfully merged {len(pdf_files)} files into {output_path}")

if __name__ == "__main__":
    pdf_merger()