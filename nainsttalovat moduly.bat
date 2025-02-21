@echo off
python.exe -m pip install --upgrade pip
pip install pyautogui %*
pip install colorama %*
pip install re %*
pip install time %*
pause