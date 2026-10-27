@echo off
echo ===================================================
echo     Launching SignBridge Full-Stack Application
echo ===================================================
echo.
echo 1. Starting Backend Signaling Server on http://localhost:5000...
start cmd /k "cd server && npm start"
timeout /t 3 /nobreak >nul

echo 2. Starting Frontend Client on http://localhost:3000...
start cmd /k "cd client && npm run dev"

echo.
echo SignBridge is starting! Open your browser at:
echo http://localhost:3000
echo.
pause
