# EcoGuide AI — Campus Sustainability Assistant

**1M1B AI for Sustainability Virtual Internship** | IBM SkillsBuild × AICTE

## Project Overview

EcoGuide AI is an AI-powered campus sustainability assistant that helps students make responsible daily choices around **waste segregation**, **water conservation**, and **carbon footprint reduction**.

### SDG Alignment
- **Primary:** SDG 12 — Responsible Consumption and Production
- **Secondary:** SDG 6 (Clean Water), SDG 11 (Sustainable Cities), SDG 13 (Climate Action)

### Problem Statement
> How might we use AI to guide students toward sustainable daily habits so that campuses can become more environmentally responsible?

Students lack quick, reliable guidance on waste bins, water-saving practices, and understanding their carbon impact. EcoGuide AI fills this gap using RAG and intelligent classification.

## Quick Start

```bash
cd ecoguide-ai
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## Run Globally (Network + Internet)

### Option 1: One-Click Local Network (Easiest)

**Windows — double-click or run:**
```powershell
.\run.bat
# or
.\run.ps1
```

**Mac/Linux:**
```bash
chmod +x run.sh && ./run.sh
```

The app binds to `0.0.0.0:8501` — accessible from:
- **This PC:** http://localhost:8501
- **Phone/other devices (same WiFi):** http://YOUR_IP:8501

### Option 2: Global Command (Run from Any Folder)

**Windows — run once:**
```powershell
powershell -ExecutionPolicy Bypass -File install-global.ps1
```

Then from **any terminal**, anywhere:
```powershell
ecoguide
```

### Option 3: Deploy to Internet (Free Cloud)

| Platform | Steps |
|----------|-------|
| **Streamlit Cloud** (recommended) | Push to GitHub → https://share.streamlit.io → New app → select repo → main file: `app.py` |
| **Render** | Connect GitHub repo → uses `render.yaml` automatically |
| **Docker** | `docker compose up` → exposes port 8501 globally |

**Streamlit Cloud (free public URL):**
1. Create GitHub repo and push this project
2. Go to https://share.streamlit.io
3. Click **New app** → select your repo
4. Main file path: `app.py`
5. Deploy → you get a URL like `https://ecoguide-ai.streamlit.app`

**Docker:**
```bash
docker compose up --build
# Access at http://localhost:8501 (or your server IP)
```

See `docs/GLOBAL_DEPLOYMENT.md` for full deployment guide.

## Project Structure

```
ecoguide-ai/
├── app.py                      # Main Streamlit application
├── requirements.txt
├── README.md
├── data/knowledge_base/        # RAG knowledge documents
│   ├── waste_segregation.txt
│   ├── water_conservation.txt
│   ├── carbon_footprint.txt
│   └── campus_sustainability.txt
├── src/
│   ├── rag_engine.py           # TF-IDF RAG pipeline
│   ├── waste_classifier.py     # NLP waste classification
│   ├── water_advisor.py        # Water usage estimation
│   ├── carbon_calculator.py    # CO2 footprint calculator
│   └── prompts.py              # Prompt templates (Granite-ready)
└── docs/
    └── PROJECT_SUBMISSION.md   # Full internship deliverable
```

## AI Components

| Component | Description |
|-----------|-------------|
| RAG | TF-IDF retrieval over sustainability knowledge base |
| Prompt Engineering | Structured prompts for each module |
| NLP Classification | Keyword-based waste categorization |
| Predictive Analytics | Water & carbon estimation models |
| Agent Workflow | Intent → Retrieve → Generate → Disclaim |

## Features

1. **Waste Segregation Guide** — Classify items into Dry/Wet/Hazardous/Reject
2. **Water Advisor** — Estimate daily usage and get personalized tips
3. **Carbon Calculator** — Daily CO2 footprint with reduction actions
4. **RAG Chat** — Ask sustainability questions grounded in knowledge base
5. **Responsible AI** — Transparency, fairness, privacy built-in

## Customization

Edit `data/knowledge_base/*.txt` to add your campus-specific policies.
Replace rule-based generation in `rag_engine.py` with IBM Granite API calls using prompts from `prompts.py`.

## License

Educational project for 1M1B Virtual Internship.
