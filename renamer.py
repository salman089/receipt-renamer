import os
import re
import pytesseract
from PIL import Image

# Point Python to your Windows Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

INPUT_DIR = 'receipts'
OUTPUT_DIR = 'processed_receipts'

# Create directories if they don't exist yet
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

"""
Acts as the AI brain. Opens the image, reads the text, 
and uses Regex to hunt for Dates and Totals.
"""


def extract_receipt_data(image_path):
    try:
        # Open the image and extract raw text
        img = Image.open(image_path)
        raw_text = pytesseract.image_to_string(img)

        # Look for Dates (Matches formats like 12/04/2026, 2026-04-12, etc.)
        date_pattern = r'(\d{1,4}[-/]\d{1,2}[-/]\d{1,4})'
        dates_found = re.findall(date_pattern, raw_text)

        # Look for Amounts (Matches numbers with two decimals, ignoring currency symbols)
        amount_pattern = r'[$£€]?\s?(\d+\.\d{2})'
        amounts_found = re.findall(amount_pattern, raw_text)

        # Clean and select the best data
        # Grab the first date found and replace slashes with dashes for safe filenames
        receipt_date = dates_found[0].replace('/', '-') if dates_found else "UNKNOWN_DATE"

        if amounts_found:
            # Convert all amounts to floats, find the maximum (which is almost always the Total)
            amounts_floats = [float(a) for a in amounts_found]
            receipt_amount = f"{max(amounts_floats):.2f}"
        else:
            receipt_amount = "UNKNOWN_AMOUNT"

        return receipt_date, receipt_amount

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return "ERROR", "ERROR"


def process_directory():
    print("🤖 Starting Smart Receipt Scanner...\n")

    # Get a list of all files in the input folder
    files = os.listdir(INPUT_DIR)

    if not files:
        print(f"No files found in the '{INPUT_DIR}' folder. Please add some images.")
        return

    # Loop through each file
    for filename in files:
        # Only process image files
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            old_path = os.path.join(INPUT_DIR, filename)

            print(f"📄 Scanning: {filename}...")

            # Send the image to our AI brain
            date, amount = extract_receipt_data(old_path)

            # Construct the new file name and path
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{date}_Total_{amount}{file_extension}"
            new_path = os.path.join(OUTPUT_DIR, new_filename)

            # Rename and move the file
            os.rename(old_path, new_path)
            print(f"✅ Renamed to: {new_filename}\n")


if __name__ == "__main__":
    process_directory()
    print("🎉 All receipts processed!")
