@echo off
echo ========================================
echo   Angry Store - Installation Check
echo ========================================
echo.

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)
echo [OK] Python is installed
echo.

echo Checking pip installation...
pip --version
if %errorlevel% neq 0 (
    echo [ERROR] pip is not installed
    pause
    exit /b 1
)
echo [OK] pip is installed
echo.

echo Checking virtual environment...
if exist "venv\" (
    echo [OK] Virtual environment exists
) else (
    echo [WARNING] Virtual environment not found
    echo Run setup.bat to create it
)
echo.

echo Checking database...
if exist "db.sqlite3" (
    echo [OK] Database exists
) else (
    echo [WARNING] Database not found
    echo Run: python manage.py migrate
)
echo.

echo Checking media folder...
if exist "media\" (
    echo [OK] Media folder exists
) else (
    echo [WARNING] Media folder not found
    mkdir media
    mkdir media\products
    mkdir media\payment_proofs
    echo [OK] Media folders created
)
echo.

echo ========================================
echo   Installation Check Complete
echo ========================================
echo.
echo Next steps:
echo 1. Run setup.bat if not done yet
echo 2. Create superuser: python manage.py createsuperuser
echo 3. Run server: python manage.py runserver
echo.
pause
