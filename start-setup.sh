#!/bin/bash

echo "?? Creating virtual environment..."
python3 -m venv venv

echo "? Activating virtual environment..."
source venv/bin/activate

echo "?? Upgrading pip..."
pip install --upgrade pip

echo "?? Installing dependencies..."
pip install -r requirements.txt

echo "? Environment setup complete. To activate it next time, run:"
echo "source venv/bin/activate"
