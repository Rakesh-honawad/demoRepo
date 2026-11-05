from shop import checkout_total


def test_checkout_without_discount():
    items = [{"price": 100, "quantity": 1}]
    assert checkout_total(items, shipping_weight=1) == 105


def test_checkout_with_tax():
    items = [{"price": 100, "quantity": 1}]
    assert checkout_total(items, shipping_weight=1, tax_rate=0.1) == 115
