"""Carbon footprint calculator for student daily activities."""

from __future__ import annotations


TRANSPORT_FACTORS = {
    "Walking/Cycling": 0.0,
    "Bus": 0.089,
    "Metro": 0.041,
    "Two-wheeler": 0.113,
    "Car (alone)": 0.192,
    "Car (carpool)": 0.048,
    "Auto-rickshaw": 0.115,
}

MEAL_FACTORS = {
    "veg": 0.5,
    "nonveg": 1.2,
    "meat": 2.5,
}


def calculate_daily_footprint(
    commute_mode: str,
    commute_km: float,
    veg_meals: int,
    nonveg_meals: int,
    meat_meals: int,
    ac_hours: float,
    laptop_hours: float,
) -> dict:
    transport_co2 = TRANSPORT_FACTORS.get(commute_mode, 0.089) * commute_km * 2

    food_co2 = (
        veg_meals * MEAL_FACTORS["veg"]
        + nonveg_meals * MEAL_FACTORS["nonveg"]
        + meat_meals * MEAL_FACTORS["meat"]
    )

    ac_co2 = ac_hours * 1.2
    laptop_co2 = laptop_hours * 0.05
    baseline_co2 = 1.5

    total = transport_co2 + food_co2 + ac_co2 + laptop_co2 + baseline_co2

    if total < 6:
        level = "Low"
        color = "green"
    elif total < 12:
        level = "Average"
        color = "orange"
    else:
        level = "High"
        color = "red"

    breakdown = {
        "Transport": round(transport_co2, 2),
        "Food": round(food_co2, 2),
        "AC": round(ac_co2, 2),
        "Electronics": round(laptop_co2, 2),
        "Baseline (daily activities)": round(baseline_co2, 2),
    }

    tips = _get_reduction_tips(commute_mode, meat_meals, ac_hours, transport_co2, food_co2, ac_co2)

    return {
        "total_kg_co2": round(total, 2),
        "level": level,
        "color": color,
        "breakdown": breakdown,
        "tips": tips,
        "weekly_goal": _weekly_goal(commute_mode, meat_meals, ac_hours),
        "annual_projection_kg": round(total * 365, 1),
    }


def _get_reduction_tips(
    commute_mode: str,
    meat_meals: int,
    ac_hours: float,
    transport_co2: float,
    food_co2: float,
    ac_co2: float,
) -> list[str]:
    tips = []
    impacts = [
        ("transport", transport_co2, "Switch 2 days/week to bus or metro — saves ~2 kg CO2/day"),
        ("food", food_co2, "Replace one meat meal with vegetarian — saves ~2 kg CO2/meal"),
        ("ac", ac_co2, "Use fan instead of AC for 2 hours — saves ~2.4 kg CO2/day"),
    ]
    impacts.sort(key=lambda x: x[1], reverse=True)

    for _, co2, tip in impacts:
        if co2 > 0.5:
            tips.append(tip)

    if commute_mode in ("Car (alone)", "Two-wheeler", "Auto-rickshaw"):
        tips.append("Try carpooling or campus bus — can cut transport emissions by 50-75%")

    if meat_meals > 0:
        tips.append("Participate in 'Meatless Monday' on campus — collective action multiplies impact")

    if ac_hours > 3:
        tips.append("Set AC to 26°C and use timer — each degree higher saves ~6% energy")

    if len(tips) < 3:
        tips.extend([
            "Use laptop power-saving mode during classes",
            "Choose local seasonal food in the cafeteria",
            "Carry a reusable bottle and avoid packaged drinks",
        ])

    return tips[:3]


def _weekly_goal(commute_mode: str, meat_meals: int, ac_hours: float) -> str:
    if commute_mode == "Car (alone)":
        return "Use bus or metro at least 3 days this week"
    if meat_meals >= 2:
        return "Limit meat meals to 2 this week"
    if ac_hours > 4:
        return "Reduce AC usage by 1 hour daily for 5 days"
    return "Track footprint daily and share one tip with a roommate"
