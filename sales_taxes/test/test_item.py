import unittest

from sales_taxes.item import Item, find_item_unit_tax_rate, parse_input_line


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

    def test_parsed_line_item_is_valid(self):
        """Check parsed item has correct types"""
        line_item = '1 music CD at 16.49'
        item = parse_input_line(line_item)

        self.assertEqual(item.name, 'music CD')
        self.assertEqual(item.quantity, 1)
        self.assertEqual(item.unit_price, 16.49)
        self.assertEqual(item.imported, False)

    def test_parsed_disordered_line_is_valid(self):

        line_item = '1 box of imported chocolates at 11.25'
        item = parse_input_line(line_item)

        self.assertEqual(item.name, 'box of chocolates')
        self.assertEqual(item.quantity, 1)
        self.assertEqual(item.unit_price, 11.25)
        self.assertEqual(item.imported, True)

