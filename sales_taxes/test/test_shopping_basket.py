import unittest
from sales_taxes.shopping_basket import ShoppingBasket, Item


class TestShoppingBasket(unittest.TestCase):
    """ ShoppingBasket class tests. """
    def setUp(self) -> None:
        self.shopping_basket = ShoppingBasket()

    def test_shopping_basket_is_empty(self):
        self.assertEqual(len(self.shopping_basket.items), 0)

    def test_check_single_item_is_in_shopping_basket(self):
        item = Item('book', 12.49, 1)
        self.shopping_basket.add_items(item)
        self.assertIn(item, self.shopping_basket.items)

    def test_check_items_are_in_shopping_basket(self):
        item1 = Item('book', 12.49, 1)
        item2 = Item('music CD', 16.49, 1)
        self.shopping_basket.add_items(item1)
        self.shopping_basket.add_items(item2)

        self.assertIn(item1, self.shopping_basket.items)
        self.assertIn(item2, self.shopping_basket.items)

    def test_total_price_of_shopping_basket(self):
        self.shopping_basket.add_items(Item('book', 12.99, 1))
        self.assertEqual(self.shopping_basket.total_price(), 12.99)

    def test_total_sales_taxes_of_shopping_basket(self):
        item = Item('music CD', 15.49, 2)
        self.shopping_basket.add_items(item)
        self.assertEqual(self.shopping_basket.total_sales_taxes(), 3.10)

    def test_added_items_total_price_and_sales_taxes_are_correct(self):
        self.shopping_basket.add_items(
            Item('bottle of perfume', 27.99, 1, imported=True),
            Item('bottle of perfume', 18.99, 1),
            Item('packet of headache pills', 9.75, 1),
            Item('box of chocolates', 11.25, 1, imported=True),
        )
        self.assertEqual(self.shopping_basket.total_price(), 74.68)
        self.assertEqual(self.shopping_basket.total_sales_taxes(), 6.7)

    def tearDown(self) -> None:
        self.shopping_basket.items.clear()


if __name__ == '__main__':
    unittest.main()
