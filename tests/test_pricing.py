from pricing import apply_discount, calculate_tax


def test_ten_percent_discount():
    assert apply_discount(100, 10) == 90


def test_zero_percent_discount():
    assert apply_discount(100, 0) == 100


def test_invalid_discount():
    assert apply_discount(100, 150) == 100


def test_calculate_tax():
    assert calculate_tax(100, 0.1) == 10
