# 📑 Smart PDF Merger

A secure, offline, and lightweight Python automation script that intelligently merges multiple PDF files into a single document. 

##  The Problem it Solves
Uploading sensitive documents (invoices, legal contracts, ID proofs) to random online PDF mergers poses a massive data privacy risk. This offline tool allows users to safely combine multiple PDF files locally on their machine in seconds. 

##  Features
* **100% Offline & Secure:** No data is uploaded to the internet.
* **Alphabetical Sorting:** Automatically sorts files before merging to ensure the sequence remains logical (e.g., `page1.pdf` followed by `page2.pdf`).
* **Smart Extension Handling:** Automatically appends `.pdf` to the final output file if the user forgets to type it.
* **Smart Filtering:** Strictly targets `.pdf` files using `pathlib.glob()`, safely ignoring any other file types in the directory.

##  Example Workflow

**Before (Multiple PDFs):**
```text
pdf_dummy_files/
├── chapter_1.pdf
├── chapter_2.pdf
└── chapter_3.pdf
```

**After Running the Script:**
```text
pdf_dummy_files/
├── chapter_1.pdf
├── chapter_2.pdf
├── chapter_3.pdf
└── final_merged_book.pdf  <-- (The new combined file)
```

 How to Use
Clone this repository to your local machine:

Bash
git clone [https://github.com/BrijeshKumarJha/smart-pdf-merger.git](https://github.com/YourUsername/smart-pdf-merger.git)
Navigate to the project directory:

Bash
cd smart-pdf-merger
Install the required external library (pypdf):

Bash
pip install pypdf
Run the script:

Bash
python merger.py
Follow the on-screen prompts to input your target folder and desired output name.

 Tech Stack
Language: Python 3

Core Library: pathlib (For extracting and handling paths)

External Package: pypdf (For robust PDF reading, appending, and writing)
