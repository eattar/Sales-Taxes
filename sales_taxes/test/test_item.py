import unittest

from sales_taxes.item import Item, find_item_tax


class TestItem(unittest.TestCase):

    def test_item_has_valid_values(self):

        item = Item('book', 12.99, 1)

        self.assertIsInstance(item.name, str)
        self.assertIsInstance(item.unit_price, float)
        self.assertIsInstance(item.quantity, int)

    # def test_item_quantity_greater_than_one(self):
    #     """Item quantity cannot be negative or zero"""
    #     item = Item('book', 12.99, 0)
    #
    #     self.assertRaises(ValueError, item.quantity)