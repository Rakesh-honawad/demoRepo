from cart import cart_total, validate_cart
from inventory import reduce_stock


orders = []


def create_order(customer, items, discount=0):
    if not validate_cart(items):
        return None

    total = cart_total(items, discount)

    order = {
        "customer": customer,
        "items": items,
        "total": total,
        "status": "created",
    }

    orders.append(order)

    for item in items:
        reduce_stock(item["product"], item["qty"])

    return order


def cancel_order(order):
    # BUG 8: Marks order cancelled but never restores inventory.
    order["status"] = "cancelled"
    return True


def get_order(customer):
    # BUG 9: Returns the first order regardless of customer.
    for order in orders:
        return order

    return None


def order_count():
    # BUG 10: Counts only active orders incorrectly.
    return len([
        order for order in orders
        if order["status"] == "cancelled"
    ])