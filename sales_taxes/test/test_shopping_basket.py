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
        self.shopping_basket.items.append(item)
        self.assertIn(item, self.shopping_basket.items)

    def test_check_items_are_in_shopping_basket(self):
        item1 = Item('book', 12.49, 1)
        item2 = Item('music CD', 16.49, 1)
        self.shopping_basket.items.append(item1)
        self.shopping_basket.items.append(item2)

        self.assertIn(item1, self.shopping_basket.items)
        self.assertIn(item2, self.shopping_basket.items)

    def tearDown(self) -> None:
        self.shopping_basket.items.clear()


if __name__ == '__main__':
    unittest.main()
