# SsTeX - Screenshot to LaTeX tool
# Copyright (C) 2026 mmichaellangelo
# 
# This script uses pyinstaller to build and bundle SsTeX as a single executable.

pyinstaller --noconsole --onefile --add-data "assets;assets" --icon "assets\icon.ico" --name "sstex" src\main.py