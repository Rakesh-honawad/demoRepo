from cart import cart_subtotal


def test_cart_subtotal():
    items = [
        {"price": 100, "quantity": 2},
        {"price": 50, "quantity": 1},
    ]
    assert cart_subtotal(items) == 250


def test_empty_cart():
    assert cart_subtotal([]) == 0


def test_multiple_quantities():
    assert cart_subtotal([{"price": 25, "quantity": 4}]) == 100
