def shipping_cost(weight_kg: float) -> float:
    """Flat 5 for up to 2 kg, then 2 per extra kg."""
    if weight_kg <= 2:
        return 5.0
    return 5.0 + (weight_kg - 2) * 20