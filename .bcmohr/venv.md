# Python virtual environment reference

## Create
Run: `python -m venv c:\path\to\myenv`

Example: `python -m venv .venv` 
- `.venv` is a common directory name (so is `venv`)

## VSCode
VSCode *should* automatically recognize the new virtual environment and ask to use it as the interpreter, but this doesn't always happen. To manually set the interpreter, press `ctrl+shift+P` and run `Python: Select Interpreter` to choose the new virtual environment.

## Activate
On Windows: `.\.venv\Scripts\activate`
On macOS/Linux: `source .venv/bin/activate`

## Deactivate
Simple run: `deactivate`