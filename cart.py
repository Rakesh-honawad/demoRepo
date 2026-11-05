def cart_subtotal(items: list[dict]) -> float:
    return sum(item["price"] * item["quantity"] for item in items)
