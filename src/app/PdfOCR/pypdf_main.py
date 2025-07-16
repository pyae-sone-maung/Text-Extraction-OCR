from  pypdf import PdfReader
import os
import re
from  src.app.AIEngine.ai_task import run_ai_text_extract

upload_dri = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
file_path = os.path.join(upload_dri, "documents", 'MM2.pdf')

def extract_clean_text(text):
    clean_text = re.sub(r'[^a-zA-Z0-9\s.,@/\u1000-\u109F\u0E00-\u0E7F]', '', text)
    clean_text = re.sub(r'\n+', '\n', clean_text)
    clean_text = "\n".join([line.strip() for line in clean_text.split('\n')])
    return clean_text

try:
    reader = PdfReader(file_path)
    num_page = len(reader.pages)
    extract_text = ""
    if num_page > 0:
        page = reader.pages[0]
        text_result = page.extract_text()
        extract_text = extract_clean_text(text_result)

    # print(extract_text)

    gemini_result = run_ai_text_extract(extract_text, "gemini")
    print(gemini_result)

    # openai_result = run_ai_text_extract(extract_text, "openai")
    # print(openai_result)

except Exception as ex:
    print(f"Error occur in pdf reading: {ex}")