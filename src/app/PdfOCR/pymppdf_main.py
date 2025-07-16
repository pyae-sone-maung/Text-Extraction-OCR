import os
import fitz

from src.app.AIEngine.ai_task import run_ai_text_extract

upload_dri = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
file_path = os.path.join(upload_dri, "documents", 'MM1.pdf')

extract_text = ""
document = fitz.open(file_path)

for page in document:
    extract_text += page.get_text()

print(extract_text)

gemini_result = run_ai_text_extract(extract_text, "gemini")
print(gemini_result)