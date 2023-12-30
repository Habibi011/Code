@echo off
where python > nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python to access the file.
) else (
    start cmd /k python SuperChatterBox.py
)
