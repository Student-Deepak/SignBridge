# SignBridge Application Launcher (PowerShell)
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "     Launching SignBridge Full-Stack Application   " -ForegroundColor Yellow
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "1. Starting Backend Signaling Server on http://localhost:5000..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd server; npm start"

Start-Sleep -Seconds 3

Write-Host "2. Starting Frontend Client on http://localhost:3000..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd client; npm run dev"

Write-Host ""
Write-Host "SignBridge is launching! Open your browser at:" -ForegroundColor Cyan
Write-Host "http://localhost:3000" -ForegroundColor White
Write-Host ""
