from cart import cart_total, validate_cart, get_item_count
from pricing import apply_discount, calculate_tax
from inventory import inventory
from orders import create_order, cancel_order, get_order, order_count


def test_discount():
    assert apply_discount(100, 10) == 90


def test_tax():
    assert calculate_tax(100, 0.18) == 118


def test_cart_total():
    items = [
        {"product": "mouse", "price": 10, "qty": 2},
        {"product": "keyboard", "price": 20, "qty": 1},
    ]
    assert cart_total(items, 10) == 36


def test_cart_validation():
    items = [{"product": "mouse", "price": 10, "qty": 2}]
    assert validate_cart(items)


def test_item_count():
    items = [
        {"product": "mouse", "price": 10, "qty": 3},
        {"product": "keyboard", "price": 20, "qty": 2},
    ]
    assert get_item_count(items) == 5


def test_order_count():
    assert order_count() == 0