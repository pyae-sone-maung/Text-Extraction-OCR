from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
import  os

upload_dri = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
docx_path = os.path.join(upload_dri, "word_documents", 'ICV.docx')


def remove_duplicate_text(raw_text):
    lines = raw_text.split('\n')

    processed_lines = []
    for line in lines:
        if '|' in line:
            parts = line.split('|')
            unique_parts = []
            seen_parts = set()
            for part in parts:
                stripped_part = part.strip()
                if stripped_part not in seen_parts:
                    seen_parts.add(stripped_part)
                    unique_parts.append(stripped_part)
            processed_line = ' | '.join(unique_parts)
            processed_lines.append(processed_line)
        else:
            processed_lines.append(line)
    return '\n'.join(processed_lines)

def extract_text_from_docx(docx_file):
    try:
        document = Document(docx_file)
        full_text = []

        for block in document.iter_inner_content():
            if isinstance(block, Paragraph):
                if block.text.strip():
                    full_text.append(block.text.strip())
            elif isinstance(block, Table):
                table_content = []
                for row_index, row in enumerate(block.rows):
                    row_data = []
                    for cell_index, cell in enumerate(row.cells):
                        cell_text = cell.text.strip()
                        row_data.append(cell_text)
                    table_content.append(" | ".join(row_data))
                full_text.append("\n".join(table_content))

        return  "\n".join(full_text)
    except Exception as ex:
        print(f"Error occur : {ex}")

text = extract_text_from_docx(docx_path)
if text is not None:
    final_result = remove_duplicate_text(text)
    print(final_result)
else:
    print("No text.")