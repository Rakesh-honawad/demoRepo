from pricing import final_price
from inventory import check_stock


def cart_total(items, discount_percent=0):
    subtotal = 0

    for item in items:
        price = item["price"]
        quantity = item["qty"]

        subtotal += price * quantity

    # BUG 5: Discount is applied to only one item instead of subtotal.
    return round(final_price(subtotal, discount_percent, 0), 2)


def validate_cart(items):
    for item in items:
        # BUG 6: Checks stock using product price instead of quantity.
        if not check_stock(item["product"], item["qty"]):
            return False

    return True


def get_item_count(items):
    # BUG 7: Returns number of distinct products, not total quantity.
    return sum(item["qty"] for item in items)