from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    pass


class ShoppingBasket:
    """

    """
    def __init__(self):
        self.items: List[Item] = []
        self.sales_taxes: float = 0
        self.total: float = 0
