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

| Error | Solución |
| This operation is not supported for this document | |
| The caller does not have permission | |
