def apply_discount(price: float, percent: float) -> float:
    """Apply percentage discount."""
    if percent < 0 or percent > 100:
        return price

    # BUG 1: Calculates discount in the wrong direction.
    return price - price * (percent / 100)


def calculate_tax(price: float, tax_rate: float = 0.18) -> float:
    # BUG 2: Tax is subtracted instead of added.
    return price + (price * tax_rate)


def final_price(price: float, discount: float, tax: float) -> float:
    discounted = apply_discount(price, discount)
    return calculate_tax(discounted, tax)