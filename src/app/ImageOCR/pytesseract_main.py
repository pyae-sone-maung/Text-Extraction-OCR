import pytesseract
from PIL import Image
import re, os
from src.app.AIEngine.ai_process import run_ai_text_extract

upload_dri = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
image_path = os.path.join(upload_dri, "images", 'thai-sample.jpg')

def extract_clean_text(text):
    clean_text = re.sub(r'[^a-zA-Z0-9\s.,@/\u1000-\u109F\u0E00-\u0E7F]', '', text)
    clean_text = re.sub(r'\n+', '\n', clean_text)
    clean_text = "\n".join([line.strip() for line in clean_text.split('\n')])
    return clean_text

try:
    img = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(img, lang='eng+mya+tha')
    ocr_result = extract_clean_text(ocr_result)

    print(ocr_result)

    # gemini_result = run_ai_text_extract(ocr_result, "gemini")
    # print(gemini_result)

except Exception as ex:
    print(f"Error during OCR : {ex}")