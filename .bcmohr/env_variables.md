# Python dotenv and environmental variables reference

## Make .env and .env.template files
Do not use quotation marks around variable values.

`.env` (should be in the .gitignore)
```
VARIABLE_ABC=123456789
API_KEY=a1b2c3d4
OTHER_VARIABLE=https://www.google.com
```

`.env.template` (include in repo)
```
VARIABLE_ABC=...
API_KEY=...
OTHER_VARIABLE=https://www.google.com
```

## Install
Check if you're inside your virtual environment, if needed. Then run: `pip install python-dotenv`

## Include in code
Include these imports:
```python
from dotenv import load_dotenv
import os
```

Include this code to call the environemental varibles:
```python
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
```

Remember that the `.env` file can be at the top of your project directory and python scripts within subdirectories can still access the top level `.env` file.
