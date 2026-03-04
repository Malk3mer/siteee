@echo off
echo ========================================
echo   ANGRY STORE - Stopping Server
echo ========================================
echo.
echo Stopping all Python processes...
taskkill /F /IM python.exe 2>nul
if %errorlevel% == 0 (
    echo.
    echo [SUCCESS] Server stopped successfully!
    echo.
) else (
    echo.
    echo [INFO] No server is running.
    echo.
)
echo ========================================
pause
