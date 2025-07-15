import math, os
import pandas as pd

upload_dri = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
file_path = os.path.join(upload_dri, "excel_documents", 'sample.xlsx')

try:
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.csv':
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='latin1')
        except Exception as ex:
            print(f"Error extraction from csv : {ex}")
            df = None

    elif file_extension == '.xlsx':
        df = pd.read_excel(file_path)
    else:
        df = None

    if df is not None:
        text_output = []
        for row_index, row in df.iterrows():
            row_output=[]
            for column_name, cell_value in row.items():
                if not (isinstance(cell_value, float) and math.isnan(cell_value)):
                    row_output.append(str(cell_value))
            if row_output:
                text_output.append((" ".join(row_output)))

        for text in text_output:
            print(text)
except Exception as ex:
    print(f"Error occur excel text extraction: {ex}")



