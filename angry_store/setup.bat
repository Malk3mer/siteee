@echo off
echo ========================================
echo   Angry Store - Setup Script
echo ========================================
echo.

echo [1/6] Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/6] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/6] Installing requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install requirements
    pause
    exit /b 1
)

echo [4/6] Creating migrations...
python manage.py makemigrations
python manage.py migrate

echo [5/6] Creating media directory...
if not exist "media" mkdir media
if not exist "media\products" mkdir media\products
if not exist "media\payment_proofs" mkdir media\payment_proofs

echo [6/6] Setup completed successfully!
echo.
echo ========================================
echo   Next Steps:
echo ========================================
echo 1. Create superuser: python manage.py createsuperuser
echo 2. Run server: python manage.py runserver
echo 3. Open browser: http://127.0.0.1:8000
echo.
pause
