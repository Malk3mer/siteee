@echo off
echo ========================================
echo   ANGRY STORE - Starting Server
echo ========================================
echo.
cd angry_store
echo Starting Django server...
python manage.py runserver
pause
