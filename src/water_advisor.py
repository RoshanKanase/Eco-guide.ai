"""Water usage advisor for campus students."""

from __future__ import annotations


def estimate_daily_usage(
    shower_minutes: float,
    tap_while_brushing: bool,
    clothes_washes_per_week: int,
    uses_bucket_bath: bool,
) -> dict:
    if uses_bucket_bath:
        shower_litres = 18
    else:
        shower_litres = shower_minutes * 12

    brushing_litres = 12 if tap_while_brushing else 0.5
    clothes_litres = (clothes_washes_per_week / 7) * 65
    cooking_litres = 8
    other_litres = 15

    total = shower_litres + brushing_litres + clothes_litres + cooking_litres + other_litres

    if total < 100:
        level = "GOOD"
        color = "green"
    elif total < 150:
        level = "MODERATE"
        color = "orange"
    else:
        level = "HIGH"
        color = "red"

    tips = []
    if shower_minutes > 5 and not uses_bucket_bath:
        tips.append(f"Reduce shower from {shower_minutes:.0f} to 5 min — saves ~{(shower_minutes-5)*12:.0f}L/day")
    if tap_while_brushing:
        tips.append("Turn off tap while brushing — saves ~11L/day")
    if clothes_washes_per_week > 3:
        tips.append("Wash clothes only with full loads — saves ~20L/day")
    if not uses_bucket_bath and shower_minutes > 3:
        tips.append("Try bucket bath (15-20L) instead of shower — saves significant water")

    tips.append("Report any leaking taps on campus — one leak wastes 10,000L/year")

    while len(tips) < 3:
        tips.append("Reuse RO reject water for mopping and toilet flushing")

    savings = 0
    if shower_minutes > 5 and not uses_bucket_bath:
        savings += (shower_minutes - 5) * 12
    if tap_while_brushing:
        savings += 11
    if clothes_washes_per_week > 3:
        savings += 15

    return {
        "daily_litres": round(total, 1),
        "level": level,
        "color": color,
        "breakdown": {
            "Bathing": round(shower_litres, 1),
            "Brushing/Hygiene": round(brushing_litres, 1),
            "Laundry (daily avg)": round(clothes_litres, 1),
            "Cooking/Drinking": round(cooking_litres, 1),
            "Other": round(other_litres, 1),
        },
        "tips": tips[:3],
        "potential_savings_litres": round(savings, 1),
        "campus_action": "Join or start a water audit in your hostel block",
    }
