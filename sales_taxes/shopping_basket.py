from typing import List
from sales_taxes.item import Item, find_item_unit_tax_rate
from sales_taxes.round_up_to_nearest_05 import roundup_nearest_05


class ShoppingBasket:
    """

    """
    def __init__(self) -> None:
        self.items: List[Item] = []
        self.items_sales_taxes: float = 0
        self.items_total_price: float = 0

    def add_items(self, *items: Item) -> None:
        """Calculates item price, including tax, and adds it to shopping basket"""
        for item in items:
            item.unit_tax_rate = find_item_unit_tax_rate(item.name) + 0.05 if item.imported else find_item_unit_tax_rate(item.name)
            item.tax = item.unit_price * item.quantity * item.unit_tax_rate
            item.price = item.unit_price * item.quantity
            self.items_sales_taxes += item.tax
            self.items_total_price += item.price
            self.items.append(item)

    def total_sales_taxes(self):
        return roundup_nearest_05(self.items_sales_taxes)

    def total_price(self):
        return round(self.items_total_price, 2) + self.total_sales_taxes()
