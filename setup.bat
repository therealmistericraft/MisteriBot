@echo off
set /P token=Enter your Token:
echo %token% > token.txt
echo Token saved successfully!

echo Setting up virtual environment...
cmd /k "python -m venv .venv & .venv\Scripts\activate & echo Installing packages... & pip install -r requirements.txt & echo Done. & cls & echo Starting MisteriBot... & python bot/src/MisteriBot.py"
