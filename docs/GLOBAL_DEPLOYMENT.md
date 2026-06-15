# EcoGuide AI — Global Deployment Guide

## 1. Run on Local Network (Same WiFi)

Anyone on your WiFi can access the app.

```powershell
# Windows
.\run.bat

# Or PowerShell
.\run.ps1
```

Find your IP:
```powershell
ipconfig
# Look for IPv4 Address (e.g. 192.168.1.5)
```

Share this URL with others: `http://192.168.1.5:8501`

**Firewall:** If others cannot connect, allow port 8501:
```powershell
New-NetFirewallRule -DisplayName "EcoGuide AI" -Direction Inbound -Port 8501 -Protocol TCP -Action Allow
```

---

## 2. Run from Any Folder (Global Command)

```powershell
powershell -ExecutionPolicy Bypass -File install-global.ps1
```

Restart terminal, then type:
```
ecoguide
```

---

## 3. Deploy to Internet — Streamlit Cloud (FREE)

Best for internship demo — get a public URL anyone can open.

### Steps:
1. **Create GitHub account** (if needed): https://github.com
2. **Create new repository** named `ecoguide-ai`
3. **Push your code:**
   ```powershell
   cd C:\Users\rosha\Projects\ecoguide-ai
   git add .
   git commit -m "EcoGuide AI - sustainability project"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ecoguide-ai.git
   git push -u origin main
   ```
4. **Deploy:** https://share.streamlit.io → Sign in with GitHub
5. **New app** → Repository: `YOUR_USERNAME/ecoguide-ai` → Branch: `main` → Main file: `app.py`
6. **Deploy** → Live URL: `https://ecoguide-ai-YOUR_USERNAME.streamlit.app`

Share this URL in your internship submission!

---

## 4. Deploy with Render (FREE tier)

1. Push code to GitHub (same as above)
2. Go to https://render.com → New → Web Service
3. Connect your GitHub repo
4. Render auto-detects `render.yaml`
5. Deploy → get URL like `https://ecoguide-ai.onrender.com`

---

## 5. Deploy with Docker (Any Server/VPS)

```bash
docker compose up --build -d
```

Works on AWS, Azure, Google Cloud, DigitalOcean, or any VPS.

---

## 6. Quick Tunnel (Temporary Public URL)

For instant demo without GitHub:

```powershell
# Install ngrok: https://ngrok.com/download
ngrok http 8501
```

ngrok gives a temporary public URL like `https://abc123.ngrok.io`

---

## Recommended for Internship Submission

| Use Case | Method |
|----------|--------|
| Demo on your laptop | `run.bat` |
| Demo on phone (same WiFi) | `run.bat` + share IP URL |
| Submit live link in PPT | **Streamlit Cloud** (permanent free URL) |
| Quick 1-hour demo | ngrok tunnel |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Port 8501 in use | Change port in `.streamlit/config.toml` |
| Others can't connect | Check Windows Firewall, allow port 8501 |
| `ecoguide` not found | Restart terminal after `install-global.ps1` |
| Streamlit Cloud build fails | Ensure `requirements.txt` has all packages |
