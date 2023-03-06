# Micro Worksheets
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Instalación

```bash
pip install git+https://github.com/lastseal/micro-worksheets
```

## Uso Básico

```python
from micro import worksheets
import os

SHEET_ID = os.getenv("SHEET_ID")

ws = worksheets.open(SHEET_ID)

print(ws)
```

## Documentación

[Crear Cuenta Bot](https://docs.gspread.org/en/v5.7.0/oauth2.html#)

## FAQ

### Error - This operation is not supported for this document

This error happens normally because the file was saved in .xlsx extension and you need to converted it to Google Sheet format by importing the excel file in your google spreadsheet instead of directly uploading it to Google Drive.
[link](https://docs.holistics.io/faqs/error-when-working-with-google-spreadsheet#:~:text=This%20error%20happens%20normally%20because,uploading%20it%20to%20Google%20Drive.)

### Error - The caller does not have permission

