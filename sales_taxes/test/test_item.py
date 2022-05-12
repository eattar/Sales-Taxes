import unittest

from sales_taxes.item import Item, find_item_tax


class TestItem(unittest.TestCase):

    def test_item_has_valid_values(self):

        item = Item('book', 12.99, 1)

        self.assertIsInstance(item.name, str)
        self.assertIsInstance(item.unit_price, float)
        self.assertIsInstance(item.quantity, int)

    def test_check_item_quantity_is_greater_than_zero(self):
        """Raises ValueError if item quantity is less or equal to zero """
        with self.assertRaises(ValueError):
            Item('book', 13.69, 0)
            Item('book', 13.69, -1)

    def test_raising_type_error_if_quantity_type_not_integer(self):
        """Raises TypeError if item quantity type is not Integer"""
        with self.assertRaises(TypeError):
            Item('book', 14.99, 0.5)
