"""Prompt templates for EcoGuide AI sustainability assistant."""

SYSTEM_PROMPT = """You are EcoGuide AI, a responsible sustainability assistant for Indian college campuses.
Your role is to help students with waste segregation, water conservation, and carbon footprint reduction.

Guidelines:
- Base answers on the provided context documents
- Be practical, actionable, and encouraging
- Align advice with UN SDGs (especially SDG 6, 11, 12, 13)
- Acknowledge uncertainty when context is insufficient
- Never provide medical, legal, or hazardous material handling advice beyond basic segregation
- Use simple language suitable for students
- Always mention which waste bin (Blue/Green/Red/Black) when relevant
"""

WASTE_CLASSIFICATION_PROMPT = """Analyze the following waste item and classify it for campus disposal in India.

Item description: {item}

Using the waste segregation guidelines, provide:
1. **Category**: Dry / Wet / Hazardous / Reject
2. **Bin Color**: Blue / Green / Red / Black
3. **Preparation Steps**: How to prepare before disposal
4. **Common Mistake**: What people often get wrong
5. **Environmental Impact**: Brief note on why correct segregation matters

Context from knowledge base:
{context}

Respond in clear, structured format."""

WATER_ADVISOR_PROMPT = """A student is asking about water conservation on campus.

Student question: {question}

Daily usage details (if provided):
- Shower minutes per day: {shower_min}
- Tap running while brushing: {tap_brushing}
- Clothes washes per week: {clothes_washes}
- Estimated daily usage: {daily_litres} litres

Context from knowledge base:
{context}

Provide:
1. **Assessment**: LOW / MODERATE / HIGH water usage
2. **Top 3 Personalized Tips**: Specific to their habits
3. **Campus Action**: One thing they can advocate for
4. **Potential Savings**: Litres saved per day if they follow tips

Be encouraging and practical."""

CARBON_ADVISOR_PROMPT = """Help a student understand their carbon footprint.

Activity profile:
- Daily commute: {commute_mode}, {commute_km} km (round trip)
- Meals today: Veg={veg_meals}, Non-veg={nonveg_meals}, Meat={meat_meals}
- AC usage: {ac_hours} hours
- Laptop usage: {laptop_hours} hours

Estimated daily CO2: {daily_co2} kg

Context from knowledge base:
{context}

Provide:
1. **Footprint Level**: Low / Average / High
2. **Breakdown**: Where most emissions come from
3. **Top 3 Reduction Actions**: Ranked by impact
4. **Weekly Goal**: One achievable target
5. **SDG Connection**: How this relates to climate action (SDG 13)"""

RAG_QA_PROMPT = """Answer the student's sustainability question using ONLY the provided context.
If the context does not contain enough information, say so and give general best-practice guidance.

Question: {question}

Retrieved context:
{context}

Provide a clear, helpful answer with bullet points where appropriate.
End with one concrete action the student can take today."""

AGENT_WORKFLOW_STEPS = [
    "Receive user query",
    "Detect intent (waste / water / carbon / general)",
    "Retrieve relevant documents from knowledge base",
    "Build context-aware prompt",
    "Generate response (LLM or rule-based fallback)",
    "Add responsible AI disclaimer",
    "Return structured answer to user",
]
