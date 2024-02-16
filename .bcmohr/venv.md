# Python virtual environment reference

## Create
Run: `python -m venv c:\path\to\myenv`

Example: `python -m venv .venv` 
- `.venv` is a common directory name (so is `venv`)
- VSCode will automatically recognize this and ask to use it as the interpreter

## Activate
On Windows: `.\.venv\Scripts\activate`
On macOS/Linux: `source .venv/bin/activate`

## Deactivate
Simple run: `deactivate`