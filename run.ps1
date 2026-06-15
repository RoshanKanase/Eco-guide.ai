# EcoGuide AI - Global Launcher (PowerShell)
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot

Write-Host ""
Write-Host "  ========================================" -ForegroundColor Green
Write-Host "   EcoGuide AI - Campus Sustainability" -ForegroundColor Green
Write-Host "   Starting global server on port 8501..." -ForegroundColor Green
Write-Host "  ========================================" -ForegroundColor Green
Write-Host ""

# Get local IP for network access
$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -notmatch 'Loopback' -and $_.IPAddress -notmatch '^169' } | Select-Object -First 1).IPAddress
if ($ip) {
    Write-Host "  Local:    http://localhost:8501" -ForegroundColor Cyan
    Write-Host "  Network:  http://${ip}:8501" -ForegroundColor Cyan
} else {
    Write-Host "  Local:    http://localhost:8501" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "  Press Ctrl+C to stop the server." -ForegroundColor Yellow
Write-Host ""

python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
