import unittest
from os import path
from sales_taxes.item import Item, parse_input_line


class TestItem(unittest.TestCase):

    def test_item_has_valid_types(self):

        item = Item('book', 12.99, 1)

        self.assertIsInstance(item.name, str)
        self.assertIsInstance(item.unit_price, float)
        self.assertIsInstance(item.quantity, int)

    def test_check_item_quantity_is_greater_than_zero(self):
        """Raises ValueError if item quantity is less or equal to zero """
        with self.assertRaises(ValueError):
            parse_input_line('0 book at 10.50')
            parse_input_line('-1 book at 10.50')

    def test_raising_type_error_if_quantity_type_not_integer(self):
        """Raises TypeError if item quantity type is not Integer"""
        with self.assertRaises(ValueError):
            parse_input_line('a book at 10.50')

    def test_parsed_line_item_is_valid(self):
        """Checks parsed item has correct types"""
        line_item = '1 music CD at 16.49'
        item = parse_input_line(line_item)

        self.assertEqual(item.name, 'music CD')
        self.assertEqual(item.quantity, 1)
        self.assertEqual(item.unit_price, 16.49)
        self.assertEqual(item.imported, False)

    def test_parsed_line_item_has_enough_values(self):
        """Checks parsed item has at least 4 substrings"""
        with self.assertRaises(Exception):
            parse_input_line('1')

    def test_there_is_at_word_before_item_price_from_input(self):
        """Checks if there is 'at' word before item price while parsing item line from user"""
        with self.assertRaises(Exception):
            parse_input_line('1 imported bottle of perfume 47.56')

    def test_parsed_line_item_name_is_string(self):
        """Checks parsed line item name if it is a string"""
        with self.assertRaises(TypeError):
            parse_input_line('1 1 at 10.00')

    def test_parsed_line_item_quantity_is_integer(self):
        """Checks parsed line item quantity if it is an integer"""
        with self.assertRaises(ValueError):
            parse_input_line('a book at 10.00')

    def test_parsed_line_item_unit_price_is_float(self):
        """Checks parsed line item unit price if it is a float"""
        with self.assertRaises(ValueError):
            parse_input_line('1 book at a')

    def test_parsed_line_item_unit_price_is_greater_than_zero(self):
        """Checks parsed line item unit price if it is a float"""
        with self.assertRaises(ValueError):
            parse_input_line('1 book at 0')
            parse_input_line('1 book at -1')

    def test_parsed_disordered_line_is_valid(self):

        line_item = '1 box of imported chocolates at 11.25'
        item = parse_input_line(line_item)

        self.assertEqual(item.name, 'box of chocolates')
        self.assertEqual(item.quantity, 1)
        self.assertEqual(item.unit_price, 11.25)
        self.assertEqual(item.imported, True)


class FindItemTaxRate(unittest.TestCase):

    def test_find_item_is_in_tax_products_db(self):
        pass
