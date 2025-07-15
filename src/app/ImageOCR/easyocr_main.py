import easyocr
import os
import re
from PIL import Image

upload_dri = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
image_path = os.path.join(upload_dri, "images", 'thai-sample1.jpg')

reader = easyocr.Reader(['th'], gpu=False)


def clean_text_from_ocr(dump_text):
    clean_text = re.sub(r'[^a-zA-Z0-9\s.,@/\u1000-\u109F\u0E00-\u0E7F]', '', text)
    clean_text = "\n".join([line.strip() for line in clean_text.split('\n')])
    return clean_text

try:
    result = reader.readtext(image_path)
    extract_text = ""
    for(bbox, text, prob) in result:
        extract_text += text + "\n"
    print(extract_text)

    final_result = clean_text_from_ocr(extract_text)
    print(final_result)
except Exception as ex:
    print(f"Error during OCR : {ex}")