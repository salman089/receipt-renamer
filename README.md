# 🤖 Smart Receipt Renamer (OCR Data Pipeline)

An automated Python utility that utilizes Optical Character Recognition (OCR) to extract unstructured text from receipt images, parses the data using Regular Expressions (Regex), and systematically renames the files based on the transaction date and total amount.

## 🚀 The Problem Solved
Digital folders often become cluttered with useless, default image filenames (e.g., `IMG_9482.jpg`). This project automates the data entry and file organization process, transforming raw images into a clean, searchable database of receipts formatted as `YYYY-MM-DD_Total_Amount.jpg`.

## 🛠️ Tech Stack & Architecture
* **Language:** Python 3.x
* **Computer Vision:** Google Tesseract OCR, PyTesseract, Pillow (PIL)
* **Data Parsing:** Python `re` (Regular Expressions)
* **File Operations:** Python `os` module

## 🧠 How It Works
1. **The Vision System:** `Pillow` loads the image into memory, and `PyTesseract` interfaces with the Tesseract engine to extract a raw text string from the pixels.
2. **The Logic Engine:** Custom Regex patterns filter through the OCR noise to isolate date formats and floating-point currency values.
3. **Deduction Algorithm:** Converts all extracted currency strings to floats and uses the `max()` function to logically deduce the final receipt total.
4. **File System Automation:** Dynamically constructs the new filename and executes OS-level rename and move commands.

## 📦 Setup & Installation

### 1. Install Tesseract OCR (Required)
This script acts as a bridge to the Tesseract engine. You must install it on your machine first.
* **Windows:** Download and install from the [UB-Mannheim repository](https://github.com/UB-Mannheim/tesseract/wiki). Ensure it is installed at `C:\Program Files\Tesseract-OCR\tesseract.exe`.

### 2. Project Setup
Clone the repository and set up your virtual environment:
git clone [https://github.com/your-username/receipt-renamer.git](https://github.com/your-username/receipt-renamer.git)  
cd receipt-renamer

# Create and activate virtual environment
python -m venv venv  
venv\Scripts\activate  # Windows

# Install Python dependencies
pip install pytesseract Pillow

### 3. Usage
Place your raw receipt images (.jpg, .jpeg, .png) into the receipts/ directory.  
Run the processing script:  
python renamer.py  
Check the processed_receipts/ directory for your cleanly renamed files!