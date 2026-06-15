"""AI-powered waste segregation classifier."""

from __future__ import annotations

import re


WASTE_RULES = [
    {
        "keywords": ["battery", "batteries", "cell", "lithium"],
        "category": "Hazardous",
        "bin": "Red / E-waste Collection",
        "prep": "Tape terminals, store in dry container, drop at e-waste drive",
        "mistake": "Throwing in regular dustbin causes soil and water contamination",
        "impact": "Prevents heavy metal leakage into environment",
    },
    {
        "keywords": ["syringe", "medicine", "tablet", "medical", "bandage"],
        "category": "Hazardous",
        "bin": "Red Bin (Bio-medical waste)",
        "prep": "Wrap safely, use designated medical waste collection only",
        "mistake": "Mixing with dry waste creates health risks for waste workers",
        "impact": "Protects sanitation workers and prevents disease spread",
    },
    {
        "keywords": ["banana", "peel", "food", "leftover", "vegetable", "fruit", "tea", "coffee", "egg shell"],
        "category": "Wet",
        "bin": "Green Bin",
        "prep": "Drain excess liquid, no plastic wrap",
        "mistake": "Putting in dry waste contaminates recyclables",
        "impact": "Enables composting and reduces methane from landfills",
    },
    {
        "keywords": ["paper", "cardboard", "notebook", "newspaper", "book"],
        "category": "Dry",
        "bin": "Blue Bin",
        "prep": "Remove plastic covers, flatten boxes, keep dry",
        "mistake": "Throwing greasy pizza boxes as dry waste",
        "impact": "Recycled paper saves trees and 60% water vs new paper",
    },
    {
        "keywords": ["plastic bottle", "pet bottle", "bottle", "container", "wrapper"],
        "category": "Dry",
        "bin": "Blue Bin",
        "prep": "Rinse, crush bottle, remove cap if required locally",
        "mistake": "Disposing with liquid or food residue inside",
        "impact": "Recycled PET reduces virgin plastic production",
    },
    {
        "keywords": ["glass", "jar", "wine bottle"],
        "category": "Dry",
        "bin": "Blue Bin",
        "prep": "Rinse, remove lids, handle carefully to avoid breakage",
        "mistake": "Mixing broken glass with other recyclables unsafely",
        "impact": "Glass is 100% recyclable without quality loss",
    },
    {
        "keywords": ["diaper", "sanitary", "napkin", "tissue", "soiled"],
        "category": "Reject",
        "bin": "Black Bin",
        "prep": "Wrap in paper, do not flush",
        "mistake": "Putting in dry or wet waste streams",
        "impact": "Prevents contamination of recyclable and compostable streams",
    },
    {
        "keywords": ["thermocol", "styrofoam", "ceramic", "broken tile"],
        "category": "Reject",
        "bin": "Black Bin",
        "prep": "Bag separately if sharp/broken",
        "mistake": "Assuming all plastic foam is recyclable",
        "impact": "Keeps recycling stream clean and efficient",
    },
    {
        "keywords": ["phone", "charger", "laptop", "cable", "earphone", "e-waste", "electronic"],
        "category": "Hazardous",
        "bin": "E-waste Collection Point",
        "prep": "Delete personal data, bring to campus e-waste drive",
        "mistake": "Discarding in dry waste or regular dustbin",
        "impact": "Recovers valuable metals and prevents toxic leaching",
    },
    {
        "keywords": ["bulb", "cfl", "tube light", "fluorescent"],
        "category": "Hazardous",
        "bin": "Red Bin / Special Collection",
        "prep": "Wrap carefully to prevent breakage, handle mercury-containing bulbs safely",
        "mistake": "Throwing in regular garbage",
        "impact": "Prevents mercury and glass hazards in landfills",
    },
]


def classify_waste(item_description: str, context: str = "") -> dict:
    """Classify waste item using keyword rules + optional RAG context."""
    text = item_description.lower()
    best_match = None
    best_score = 0

    for rule in WASTE_RULES:
        score = sum(1 for kw in rule["keywords"] if kw in text)
        if score > best_score:
            best_score = score
            best_match = rule

    if best_match and best_score > 0:
        return {
            "item": item_description,
            "category": best_match["category"],
            "bin": best_match["bin"],
            "preparation": best_match["prep"],
            "common_mistake": best_match["mistake"],
            "environmental_impact": best_match["impact"],
            "confidence": "High" if best_score >= 2 else "Medium",
            "method": "Rule-based NLP classification",
        }

    return {
        "item": item_description,
        "category": "Dry (likely)",
        "bin": "Blue Bin — verify locally",
        "preparation": "Clean and dry the item before disposal",
        "common_mistake": "Mixing with food waste",
        "environmental_impact": "Proper sorting improves recycling rates",
        "confidence": "Low",
        "method": "Fallback classification — please verify with campus facilities",
        "rag_hint": _extract_hint_from_context(context),
    }


def _extract_hint_from_context(context: str) -> str:
    for line in context.split("\n"):
        if line.strip().startswith("-"):
            return line.strip()
    return "Check campus waste guidelines for this item."
