from cart import cart_total

def test_no_discount():
    assert cart_total([{"price": 10.0, "qty": 2}]) == 20.0

def test_ten_percent_discount():
    items = [{"price": 50.0, "qty": 2}]
    assert cart_total(items, discount_percent=10) == 90.0
