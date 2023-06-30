@echo off
cd /d "D:\Study\2023-sum\crawling"
start /B python app.py
ping 127.0.0.1 -n 11 > nul
start chrome.exe http://127.0.0.1:5000/
