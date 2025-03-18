name: Test YOLO inference API

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Check Python syntax
        run: |
          python -m py_compile app.py
      - name: Check if model file exists
        run: |
          test -f model/my_model.pt && echo "Model exists" || echo "Model missing"
