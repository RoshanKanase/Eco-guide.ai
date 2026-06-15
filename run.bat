@echo off
title EcoGuide AI - Global Server
cd /d "%~dp0"

echo.
echo  ========================================
echo   EcoGuide AI - Campus Sustainability
echo   Starting global server on port 8501...
echo  ========================================
echo.
echo   Local:    http://localhost:8501
echo   Network:  http://YOUR_IP:8501
echo.
echo   Press Ctrl+C to stop the server.
echo.

python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
