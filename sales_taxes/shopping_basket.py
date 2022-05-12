from typing import List
from sales_taxes.item import Item


class ShoppingBasket:
    """

    """
    def __init__(self):
        self.items: List[Item] = []
        self.sales_taxes: float = 0
        self.total: float = 0
