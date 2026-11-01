inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15,
}


def check_stock(product: str, quantity: int) -> bool:
    # BUG 3: Allows orders when requested quantity exceeds stock.
    return inventory.get(product, 0) >= 0


def reduce_stock(product: str, quantity: int) -> bool:
    if not check_stock(product, quantity):
        return False

    # BUG 4: Subtracts quantity twice.
    inventory[product] -= quantity
    inventory[product] -= quantity
    return True


def restock(product: str, quantity: int):
    inventory[product] = inventory.get(product, 0) - quantity