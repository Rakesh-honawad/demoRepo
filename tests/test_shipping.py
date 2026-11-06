from shipping import shipping_cost


def test_light_parcel():
    assert shipping_cost(1) == 5


def test_heavy_parcel():
    assert shipping_cost(5) == 11
