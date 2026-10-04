@echo off
call "%~dp0.venv\Scripts\activate.bat"
if "%~1"=="" (
    set /p MINS=Enter sleep timer in minutes: 
) else (
    set MINS=%~1
)
python "%~dp0sleep_timer.py" %MINS%
pause
