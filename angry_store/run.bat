@echo off
echo ========================================
echo   Starting Angry Store Server...
echo ========================================
echo.

call venv\Scripts\activate.bat
python manage.py runserver

pause
