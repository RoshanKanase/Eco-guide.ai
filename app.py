"""
EcoGuide AI — Campus Sustainability Assistant
1M1B AI for Sustainability Virtual Internship Project
"""

import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.carbon_calculator import calculate_daily_footprint
from src.prompts import AGENT_WORKFLOW_STEPS, SYSTEM_PROMPT
from src.rag_engine import RAGEngine
from src.waste_classifier import classify_waste
from src.water_advisor import estimate_daily_usage

KNOWLEDGE_DIR = ROOT / "data" / "knowledge_base"

st.set_page_config(
    page_title="EcoGuide AI — Campus Sustainability",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
    .main-header {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #43a047 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 1.5rem;
    }
    .sdg-badge {
        background: #e8f5e9;
        color: #1b5e20;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin-right: 0.5rem;
        display: inline-block;
    }
    .metric-card {
        background: #f1f8e9;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2e7d32;
    }
    .disclaimer {
        background: #fff3e0;
        padding: 1rem;
        border-radius: 8px;
        font-size: 0.9rem;
        border-left: 4px solid #ff9800;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


@st.cache_resource
def load_rag():
    return RAGEngine(KNOWLEDGE_DIR)


def render_header():
    st.markdown(
        """
        <div class="main-header">
            <h1>🌱 EcoGuide AI</h1>
            <p>Campus Sustainability Assistant — Powered by RAG + Responsible AI</p>
            <span class="sdg-badge">SDG 12: Responsible Consumption</span>
            <span class="sdg-badge">SDG 6: Clean Water</span>
            <span class="sdg-badge">SDG 13: Climate Action</span>
            <span class="sdg-badge">SDG 11: Sustainable Cities</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_home():
    render_header()
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Problem We Solve")
        st.markdown(
            """
            **How might we use AI to guide students toward sustainable daily habits
            so that campuses can become more environmentally responsible?**

            Students on Indian campuses often lack quick, reliable guidance on:
            - Which bin to use for different waste items
            - How to reduce water consumption in hostels
            - Understanding personal carbon footprint from daily choices

            EcoGuide AI bridges this gap using **Retrieval-Augmented Generation (RAG)**
            and **intelligent classification** over a curated sustainability knowledge base.
            """
        )

        st.subheader("AI Components Used")
        st.markdown(
            """
            | Component | Purpose |
            |-----------|---------|
            | **RAG Pipeline** | Retrieves campus sustainability policies & guidelines |
            | **Prompt Engineering** | Structured prompts for waste, water, carbon advice |
            | **NLP Classification** | Waste item categorization (Dry/Wet/Hazardous/Reject) |
            | **Predictive Analytics** | Water usage & carbon footprint estimation |
            | **Agent Workflow** | Intent detection → Retrieve → Generate → Disclaim |
            """
        )

    with col2:
        st.subheader("Target Users")
        st.markdown(
            """
            - College students & hostel residents
            - Campus eco-club volunteers
            - Facility management teams
            - Sustainability coordinators
            """
        )
        st.subheader("Expected Impact")
        st.markdown(
            """
            - **30%** better waste segregation accuracy
            - **20%** water savings through awareness
            - Measurable carbon tracking per student
            - Faster policy access via AI chat
            """
        )


def page_waste_classifier():
    st.header("♻️ AI Waste Segregation Guide")
    st.caption("SDG 12 — Responsible Consumption and Production")

    rag = load_rag()
    item = st.text_input(
        "Describe a waste item",
        placeholder="e.g., plastic water bottle, banana peel, old phone charger",
    )

    if st.button("Classify Waste", type="primary") and item:
        context = rag.format_context(rag.retrieve(item))
        result = classify_waste(item, context)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Category", result["category"])
        with col2:
            st.metric("Bin", result["bin"])
        with col3:
            st.metric("Confidence", result["confidence"])

        st.markdown(f"**Preparation:** {result['preparation']}")
        st.markdown(f"**Common Mistake:** {result['common_mistake']}")
        st.markdown(f"**Environmental Impact:** {result['environmental_impact']}")
        st.caption(f"Method: {result['method']}")

        with st.expander("View RAG Context Retrieved"):
            st.text(context[:800])

    st.divider()
    st.subheader("Try These Examples")
    examples = ["Banana peel", "Plastic bottle", "Old laptop charger", "Sanitary napkin", "Pizza box with grease"]
    cols = st.columns(len(examples))
    for col, ex in zip(cols, examples):
        if col.button(ex, key=f"ex_{ex}"):
            st.session_state["waste_example"] = ex
    if "waste_example" in st.session_state:
        st.info(f"Selected: {st.session_state['waste_example']} — enter it above and click Classify")


def page_water_advisor():
    st.header("💧 Smart Water Usage Advisor")
    st.caption("SDG 6 — Clean Water and Sanitation")

    col1, col2 = st.columns(2)
    with col1:
        shower = st.slider("Shower duration (minutes/day)", 0, 30, 10)
        bucket = st.checkbox("I use bucket bath instead of shower")
        tap_brush = st.checkbox("I leave tap running while brushing")
    with col2:
        washes = st.slider("Clothes washes per week", 0, 7, 2)

    if st.button("Analyze Water Usage", type="primary"):
        result = estimate_daily_usage(shower, tap_brush, washes, bucket)

        level_colors = {"GOOD": "🟢", "MODERATE": "🟡", "HIGH": "🔴"}
        st.metric(
            "Estimated Daily Usage",
            f"{result['daily_litres']} L",
            delta=f"{level_colors[result['level']]} {result['level']}",
        )

        st.subheader("Usage Breakdown")
        for key, val in result["breakdown"].items():
            st.progress(min(val / 150, 1.0), text=f"{key}: {val} L")

        st.subheader("Personalized Tips")
        for tip in result["tips"]:
            st.markdown(f"- {tip}")

        st.success(f"Potential savings: **{result['potential_savings_litres']} L/day** if you follow tips")
        st.info(f"**Campus Action:** {result['campus_action']}")


def page_carbon_calculator():
    st.header("🌍 Carbon Footprint Estimator")
    st.caption("SDG 13 — Climate Action")

    col1, col2 = st.columns(2)
    with col1:
        commute = st.selectbox(
            "Daily commute mode",
            ["Walking/Cycling", "Bus", "Metro", "Two-wheeler", "Car (alone)", "Car (carpool)", "Auto-rickshaw"],
        )
        km = st.number_input("One-way distance (km)", 0.0, 50.0, 5.0)
    with col2:
        veg = st.number_input("Vegetarian meals today", 0, 5, 2)
        nonveg = st.number_input("Non-veg (chicken/eggs) meals", 0, 5, 1)
        meat = st.number_input("Red meat meals", 0, 3, 0)
        ac_hrs = st.number_input("AC usage (hours)", 0.0, 24.0, 2.0)
        laptop_hrs = st.number_input("Laptop usage (hours)", 0.0, 16.0, 6.0)

    if st.button("Calculate Footprint", type="primary"):
        result = calculate_daily_footprint(commute, km, veg, nonveg, meat, ac_hrs, laptop_hrs)

        st.metric("Daily CO₂ Footprint", f"{result['total_kg_co2']} kg", delta=result["level"])
        st.caption(f"Annual projection: {result['annual_projection_kg']} kg CO₂/year")

        st.subheader("Emission Breakdown")
        for source, kg in result["breakdown"].items():
            pct = (kg / result["total_kg_co2"]) * 100 if result["total_kg_co2"] else 0
            st.progress(min(pct / 100, 1.0), text=f"{source}: {kg} kg ({pct:.0f}%)")

        st.subheader("Top Reduction Actions")
        for tip in result["tips"]:
            st.markdown(f"- {tip}")

        st.success(f"**Weekly Goal:** {result['weekly_goal']}")


def page_rag_chat():
    st.header("🤖 Sustainability Knowledge Chat (RAG)")
    st.caption("Ask anything about campus sustainability — answers grounded in knowledge base")

    rag = load_rag()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.text_input(
        "Your question",
        placeholder="e.g., How can our campus reduce plastic waste during events?",
    )

    if st.button("Ask EcoGuide", type="primary") and question:
        with st.spinner("Retrieving context and generating answer..."):
            response = rag.answer_question(question)
        st.session_state.chat_history.append((question, response))

    for q, resp in reversed(st.session_state.chat_history):
        with st.chat_message("user"):
            st.write(q)
        with st.chat_message("assistant"):
            st.markdown(resp["answer"])
            st.caption(f"Sources: {', '.join(resp['sources'])}")

    with st.expander("RAG Pipeline Architecture"):
        st.code(
            """
User Query
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity Search (Top-K chunks)
    ↓
Context Assembly from knowledge_base/
    ↓
Prompt Construction (prompts.py)
    ↓
Response Generation (rule-based / LLM-ready)
    ↓
Responsible AI Disclaimer
            """,
            language="text",
        )


def page_workflow():
    st.header("📋 AI Workflow & Responsible AI")
    st.subheader("Agent Workflow")
    for i, step in enumerate(AGENT_WORKFLOW_STEPS, 1):
        st.markdown(f"**Step {i}:** {step}")

    st.divider()
    st.subheader("Responsible AI Considerations")
    st.markdown(
        """
        | Principle | How EcoGuide AI Addresses It |
        |-----------|------------------------------|
        | **Fairness** | Advice is general for all students; no profiling by income/region |
        | **Transparency** | Shows retrieved sources, classification method, and confidence levels |
        | **Ethics** | No harmful advice; hazardous items directed to proper collection |
        | **Privacy** | No personal data stored; all inputs processed in-session only |
        | **Accuracy** | Low-confidence classifications flagged; users advised to verify locally |
        | **Human Oversight** | AI provides guidance, not enforcement — facility teams make final decisions |
        """
    )

    st.markdown(
        '<div class="disclaimer">⚠️ <b>Disclaimer:</b> EcoGuide AI provides educational guidance only. '
        "Always follow your campus and municipal waste/water policies. "
        "For hazardous materials, contact authorized collection services.</div>",
        unsafe_allow_html=True,
    )

    st.divider()
    st.subheader("System Prompt (for IBM Granite / LLM integration)")
    st.code(SYSTEM_PROMPT, language="text")


def main():
    st.sidebar.title("🌱 EcoGuide AI")
    st.sidebar.caption("1M1B × IBM SkillsBuild × AICTE")
    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "Navigate",
        [
            "🏠 Home",
            "♻️ Waste Classifier",
            "💧 Water Advisor",
            "🌍 Carbon Calculator",
            "🤖 RAG Chat",
            "📋 Workflow & Ethics",
        ],
    )

    pages = {
        "🏠 Home": page_home,
        "♻️ Waste Classifier": page_waste_classifier,
        "💧 Water Advisor": page_water_advisor,
        "🌍 Carbon Calculator": page_carbon_calculator,
        "🤖 RAG Chat": page_rag_chat,
        "📋 Workflow & Ethics": page_workflow,
    }
    pages[page]()

    st.sidebar.markdown("---")
    st.sidebar.info(
        "**Project:** EcoGuide AI\n\n"
        "**Internship:** 1M1B AI for Sustainability\n\n"
        "**Tech:** Python, Streamlit, RAG, NLP"
    )


if __name__ == "__main__":
    main()
