from dataclasses import dataclass


@dataclass
class Item:
    """ class for items added """

    name: str
    unit_price: float
    quantity: int
    imported: bool = False
    total_price: float = None
    unit_tax: float = None


def find_item_tax(item):

    if item in ['book', 'chocolate bar', 'packet of headache pills', 'box of chocolates']:
        return 0
    else:
        return 0.10
