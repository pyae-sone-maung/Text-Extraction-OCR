from pdfminer.high_level import extract_text
import  os
import re
from src.app.AIEngine.ai_process import run_ai_text_extract

upload_dri = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
file_path = os.path.join(upload_dri, "documents", 'MMM.pdf')

def extract_clean_text(text):
    clean_text = re.sub(r'[^a-zA-Z0-9\s.,@/\u1000-\u109F\u0E00-\u0E7F]', '', text)
    clean_text = re.sub(r'\n+', '\n', clean_text)
    clean_text = "\n".join([line.strip() for line in clean_text.split('\n')])
    return clean_text

try:
    text_result = extract_text(file_path)
    final_result = extract_clean_text(text_result)

    print(final_result)
    test_result = run_ai_text_extract(final_result, "gemini")
    print(test_result)
except Exception as ex:
    print(f"Error occur: {ex}")