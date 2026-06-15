# EcoGuide AI - Install Global Launcher (Windows)
# Run once: Right-click -> Run with PowerShell
# Or: powershell -ExecutionPolicy Bypass -File install-global.ps1

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$GlobalDir = Join-Path $env:USERPROFILE "AppData\Local\EcoGuideAI"
$LauncherPath = Join-Path $GlobalDir "ecoguide.bat"

Write-Host "Installing EcoGuide AI global launcher..." -ForegroundColor Green

# Create global launcher directory
New-Item -ItemType Directory -Force -Path $GlobalDir | Out-Null

# Create launcher that always runs from project folder
@"
@echo off
cd /d "$ProjectRoot"
python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
"@ | Set-Content -Path $LauncherPath -Encoding ASCII

# Add to user PATH if not already present
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*$GlobalDir*") {
    [Environment]::SetEnvironmentVariable("Path", "$userPath;$GlobalDir", "User")
    $env:Path = "$env:Path;$GlobalDir"
    Write-Host "Added to PATH: $GlobalDir" -ForegroundColor Cyan
} else {
    Write-Host "Already in PATH: $GlobalDir" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "  SUCCESS! EcoGuide AI is now globally available." -ForegroundColor Green
Write-Host ""
Write-Host "  Run from ANY folder:" -ForegroundColor White
Write-Host "    ecoguide" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Access URLs:" -ForegroundColor White
Write-Host "    http://localhost:8501" -ForegroundColor Cyan
Write-Host "    http://YOUR_IP:8501  (other devices on same WiFi)" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Restart terminal, then type: ecoguide" -ForegroundColor Yellow
Write-Host ""
