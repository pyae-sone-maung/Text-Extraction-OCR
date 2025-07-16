import pytesseract
from PIL import Image
import re
import os

upload_dri = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
image_path = os.path.join(upload_dri, "images", 'myanmar-sample.jpg')

def extract_clean_text(text):
    clean_text = re.sub(r'[^a-zA-Z0-9\s.,@/\u1000-\u109F\u0E00-\u0E7F]', '', text)
    clean_text = re.sub(r'\n+', '\n', clean_text)
    clean_text = "\n".join([line.strip() for line in clean_text.split('\n')])
    return clean_text

try:
    img = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(img, lang='eng+mya+tha')
    final_result = extract_clean_text(ocr_result)

    print(final_result)
except Exception as ex:
    print(f"Error during OCR : {ex}")