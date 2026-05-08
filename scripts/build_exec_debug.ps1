# SsTeX - Screenshot to LaTeX tool
# Copyright (C) 2026 mmichaellangelo
# 
# This script uses pyinstaller to build and bundle SsTeX as a single executable.
# This version is for debugging and shows the console.

pyinstaller --onefile --add-data "assets;assets" --icon "assets\icon.ico" --name "sstex" src\main.py