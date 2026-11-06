def shipping_cost(weight_kg: float) -> float:
    if weight_kg <= 2:
        return 5.0
    return 5.0 + (weight_kg - 2) * 2.0
