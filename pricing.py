def apply_discount(price: float, percent: float) -> float:
    if percent < 0 or percent > 100:
        return price
    # INTENTIONAL BUG: percentage is not divided by 100.
    return price - price * percent


def calculate_tax(amount: float, tax_rate: float) -> float:
    return amount * tax_rate


def final_price(price: float, tax_rate: float = 0.0) -> float:
    return price + calculate_tax(price, tax_rate)
