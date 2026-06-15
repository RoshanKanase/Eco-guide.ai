# EcoGuide AI — Project Submission Document
## 1M1B AI for Sustainability Virtual Internship

---

## Slide 1: Title Slide

**Project Title:** EcoGuide AI — Campus Sustainability Assistant

**Student Name(s):** [Your Name Here]

**College Name:** [Your College Name Here]

**Internship:** 1M1B AI for Sustainability Virtual Internship (IBM SkillsBuild × AICTE)

**Date:** June 2026

---

## Slide 2: SDG Alignment

### Primary SDG
**SDG 12: Responsible Consumption and Production**
- Target 12.5: Substantially reduce waste generation through prevention, reduction, recycling
- Target 12.8: Ensure people have relevant information for sustainable development

### Secondary SDGs
| SDG | Connection |
|-----|------------|
| SDG 6 | Water conservation advisor for hostel students |
| SDG 11 | Sustainable campus community practices |
| SDG 13 | Carbon footprint tracking and climate action tips |

---

## Slide 3: Problem Statement

### The Problem
On Indian college campuses, thousands of students generate waste, consume water, and commute daily — yet most lack:
- Clear guidance on **which bin** to use for different items
- Awareness of **personal water consumption** patterns
- Understanding of **daily carbon footprint** from food, transport, and energy

### Who Is Affected?
- Students and hostel residents
- Campus sanitation workers (improper segregation affects their safety)
- Local environment (landfills, water tables, air quality)
- Future generations (climate impact)

### Why Does It Persist?
- Sustainability policies are buried in PDFs students never read
- No instant, personalized guidance at point of decision
- Lack of feedback loops on daily habits

### Formal Problem Statement
> **How might we use AI to guide students toward sustainable daily habits so that campuses can become more environmentally responsible?**

---

## Slide 4: Design Thinking Process

### 1. Empathize
- Observed confusion at campus waste bins during events
- Hostel mates running taps while brushing teeth
- Friends unaware that daily commute mode significantly affects CO2

### 2. Define
- **Users:** College students, eco-club volunteers
- **Gap:** No accessible, instant sustainability advisor
- **Need:** Decision support at moment of action

### 3. Ideate
- Waste classification chatbot
- Water usage calculator with tips
- Carbon footprint estimator
- RAG system for campus policies

### 4. Prototype
- Built working Streamlit web app
- 4 knowledge base documents for RAG
- 5 AI modules integrated

### 5. Test & Refine
- Tested with sample waste items (banana peel, charger, pizza box)
- Validated water estimates against WHO benchmarks
- Added confidence levels and disclaimers

---

## Slide 5: AI Solution Overview

### Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Student    │────▶│  Streamlit   │────▶│  Intent Router  │
│  (Browser)  │     │  Web App     │     │  (Module Select)│
└─────────────┘     └──────────────┘     └────────┬────────┘
                                                   │
                    ┌──────────────────────────────┼──────────────────────────────┐
                    ▼                              ▼                              ▼
           ┌────────────────┐           ┌────────────────┐           ┌────────────────┐
           │ Waste          │           │ Water / Carbon │           │ RAG Chat       │
           │ Classifier     │           │ Advisors       │           │ Engine         │
           └───────┬────────┘           └───────┬────────┘           └───────┬────────┘
                   │                            │                            │
                   └────────────────────────────┼────────────────────────────┘
                                                ▼
                                    ┌───────────────────────┐
                                    │ Knowledge Base (TXT)  │
                                    │ + Prompt Templates    │
                                    └───────────────────────┘
```

### AI Techniques Used
1. **Retrieval-Augmented Generation (RAG)** — TF-IDF + cosine similarity
2. **Prompt Engineering** — Structured templates for Granite/LLM integration
3. **NLP Classification** — Keyword-based waste categorization
4. **Predictive Analytics** — Water and carbon estimation models
5. **Agentic Workflow** — Multi-step: detect → retrieve → generate → disclaim

---

## Slide 6: Target Users

| User Group | How They Benefit |
|------------|------------------|
| **Students** | Instant guidance on waste, water, carbon choices |
| **Eco-club volunteers** | Tool for awareness drives and peer education |
| **Hostel wardens** | Water usage awareness campaigns |
| **Facility managers** | Reduced contamination in waste streams |
| **Sustainability coordinators** | Scalable digital companion to policies |

---

## Slide 7: Prototype Demo

### Modules Built (Working Prototype)

1. **Waste Classifier** — Input: "plastic bottle" → Output: Dry/Blue bin + prep steps
2. **Water Advisor** — Input: shower minutes, habits → Output: daily litres + 3 tips
3. **Carbon Calculator** — Input: commute, meals, AC → Output: kg CO2/day + reduction plan
4. **RAG Chat** — Input: free-text question → Output: grounded answer with sources
5. **Workflow & Ethics** — Transparency dashboard

### How to Run Demo
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Screenshots to Capture
- Home page with SDG badges
- Waste classification result for "old phone charger"
- Water advisor showing HIGH/MODERATE/GOOD rating
- Carbon breakdown chart
- RAG chat with source citations

---

## Slide 8: Prompt Workflow Examples

### Waste Classification Prompt
```
Analyze the following waste item and classify it for campus disposal in India.
Item: {item}
Context: {retrieved_knowledge}
Provide: Category, Bin Color, Preparation, Common Mistake, Impact
```

### RAG Q&A Prompt
```
Answer using ONLY the provided context.
Question: {question}
Context: {top_k_chunks}
End with one concrete action for today.
```

### System Prompt (Granite-ready)
```
You are EcoGuide AI, a responsible sustainability assistant for Indian college campuses.
Base answers on context. Align with SDGs. Acknowledge uncertainty. No harmful advice.
```

---

## Slide 9: Responsible AI Considerations

| Principle | Implementation |
|-----------|----------------|
| **Fairness** | No demographic profiling; advice applies equally to all students |
| **Transparency** | Shows classification confidence, retrieved sources, and calculation breakdown |
| **Ethics** | Hazardous items directed to proper collection; no dangerous DIY advice |
| **Privacy** | No data stored server-side; session-only processing |
| **Accuracy** | Low-confidence results flagged; users told to verify with local rules |
| **Accountability** | Clear disclaimer: AI guidance, not regulatory enforcement |
| **Inclusion** | Simple language; works without smartphone apps (web-based) |

---

## Slide 10: Expected Impact

### If Implemented on a 5,000-Student Campus

| Metric | Current (Est.) | With EcoGuide AI | Improvement |
|--------|----------------|------------------|-------------|
| Waste segregation accuracy | ~40% | ~70% | +30% |
| Avg. daily water use/student | 130L | 104L | -20% |
| Students tracking carbon | <5% | 40%+ | Awareness ↑ |
| Policy query response time | Days (manual) | Seconds (RAG) | 99% faster |

### Who Benefits?
- **Sanitation workers:** Less exposure to hazardous mixed waste
- **Students:** Actionable habits, gamifiable footprint tracking
- **Administration:** Data for sustainability reporting (AICTE Green Campus)
- **Environment:** Less landfill, lower methane, reduced groundwater stress

### Long-term Vision
- Integrate with campus IoT (smart meters, bin sensors)
- Connect to IBM Granite for natural language responses
- Multi-language support (Hindi, regional languages)
- Department-level sustainability leaderboards

---

## Slide 11: Key Learnings

- AI for sustainability doesn't need to be complex — **clarity of thought** matters most
- RAG makes AI **trustworthy** by grounding answers in real policies
- **Responsible AI** is not a slide — it's built into confidence scores and disclaimers
- Small daily habits × thousands of students = **massive collective impact**

---

## Slide 12: Thank You

**EcoGuide AI** — Demonstrating how AI can be a force for sustainability, inclusion, and positive change.

**Repository:** `ecoguide-ai/`
**Run:** `streamlit run app.py`

*Built for 1M1B AI for Sustainability Virtual Internship*

---

## Appendix: File Checklist for Submission

- [x] Project Description (this document)
- [x] SDG Alignment
- [x] Problem Statement
- [x] AI Solution Overview
- [x] Target Users
- [x] Responsible AI Considerations
- [x] Expected Impact
- [x] Working Prototype (`app.py`)
- [x] RAG Demo (knowledge base + chat module)
- [x] Prompt workflows (`src/prompts.py`)
- [x] Flow diagrams (in this document)

**To convert to PPT/PDF:** Copy each slide section into PowerPoint or Google Slides. Add screenshots from the running app.
