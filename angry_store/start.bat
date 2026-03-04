@echo off
chcp 65001 >nul
cls
color 0C
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                                                              ║
echo ║              🎮 ANGRY STORE - Starting... 🔥                 ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 🔐 Login: malk / malk20101512
echo 🌐 URL: http://127.0.0.1:8000
echo.
echo Starting server...
echo.

cd /d "%~dp0"

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    python manage.py runserver 127.0.0.1:8000
) else (
    python manage.py runserver 127.0.0.1:8000
)

pause
