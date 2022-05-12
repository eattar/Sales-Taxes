import unittest
from sales_taxes.shopping_basket import ShoppingBasket
from sales_taxes.item import Item
from sales_taxes.checkout import add_items, parse_input_line, round_05


class TestCheckout(unittest.TestCase):

    def test_add_items_to_shopping_basket(self):

        shopping_basket = ShoppingBasket()
        item = Item('book', 12.49, 1)
        add_items(shopping_basket, item)
        self.assertIn(item, shopping_basket.items)

    def test_parsed_line_item_is_valid(self):

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

    def test_total_price_of_added_items_is_correct(self):

        item1 = parse_input_line('1 book at 12.49')
        item2 = parse_input_line('1 music CD at 14.99')
        item3 = parse_input_line('1 chocolate bar at 0.85')

        shopping_basket = ShoppingBasket()
        add_items(shopping_basket, item1, item2, item3)
        self.assertAlmostEqual(29.83, round(shopping_basket.total, 2))

    def test_sales_taxes_of_added_items_is_correct(self):
        item1 = parse_input_line('1 music CD at 14.99')
        item2 = parse_input_line('1 book at 12.49')
        item3 = parse_input_line('1 chocolate bar at 0.85')

        shopping_basket = ShoppingBasket()
        add_items(shopping_basket, item1, item2, item3)
        self.assertAlmostEqual(1.5, round(shopping_basket.sales_taxes, 2))

    def test_sales_taxes_of_added_imported_items_is_correct(self):
        item1 = parse_input_line('1 imported box of chocolates at 10.00')
        item2 = parse_input_line('1 imported bottle of perfume at 47.50')

        shopping_basket = ShoppingBasket()
        add_items(shopping_basket, item1, item2)
        self.assertAlmostEqual(65.12, round(shopping_basket.total, 2))
        self.assertAlmostEqual(7.60, round_05(shopping_basket.sales_taxes))

    def test_sales_taxes_of_added_mixed_items_is_correct(self):
        item_1 = parse_input_line('1 imported bottle of perfume at 27.99')
        item_2 = parse_input_line('1 bottle of perfume at 18.99')
        item_3 = parse_input_line('1 packet of headache pills at 9.75')
        item_4 = parse_input_line('1 box of imported chocolates at 11.25')

        shopping_basket = ShoppingBasket()
        add_items(shopping_basket, item_1, item_2, item_3, item_4)
        self.assertAlmostEqual(6.65, round_05(shopping_basket.sales_taxes))
        self.assertAlmostEqual(74.64, round(shopping_basket.total, 2))