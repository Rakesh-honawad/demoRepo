from cart import cart_subtotal
from pricing import apply_discount, calculate_tax
from shipping import shipping_cost


def checkout_total(
    items: list[dict],
    shipping_weight: float,
    discount_percent: float = 0,
    tax_rate: float = 0,
) -> float:
    subtotal = cart_subtotal(items)
    discounted = apply_discount(subtotal, discount_percent)
    taxed = discounted + calculate_tax(discounted, tax_rate)
    return taxed + shipping_cost(shipping_weight)
