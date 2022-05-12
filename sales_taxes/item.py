

class Item:
    """ class for items added to shopping basket"""
    def __init__(self, name: str, unit_price: float, quantity: int, imported: bool = False, total_price: float = None,
                 unit_tax: float = None) -> None:
        self.name = name

        if unit_price <= 0:
            raise ValueError("Item unit price cannot be equal or less than zero")
        elif not isinstance(unit_price, float):
            raise TypeError("Item unit price should be a float")
        else:
            self.unit_price = unit_price

        if quantity <= 0:
            raise ValueError("Item quantity cannot be equal or less than zero")
        elif not isinstance(quantity, int):
            raise TypeError("Item quantity must be an integer")
        else:
            self.quantity = quantity

        self.imported = imported
        self.total_price = total_price
        self.unit_tax = unit_tax


def find_item_tax(name) -> float:

    if name in ['book', 'chocolate bar', 'packet of headache pills', 'box of chocolates']:
        return 0
    else:
        return 0.10
