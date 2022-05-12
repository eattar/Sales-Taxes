from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    """ class for items added """

    name: str
    unit_price: float
    quantity: int
    imported: bool = False
    total_price: float = None
    unit_tax: float = None


class ShoppingBasket:
    """

    """
    def __init__(self):
        self.items: List[Item] = []
        self.sales_taxes: float = 0
        self.total: float = 0
