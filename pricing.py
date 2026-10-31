def apply_discount(price: float, percent: float) -> float:
    """Return the price after a percentage discount (percent is 0-100)."""
    return price - price * percent
