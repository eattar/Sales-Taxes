import unittest
from sales_taxes.shopping_basket import ShoppingBasket, Item


class TestShoppingBasket(unittest.TestCase):
    """ ShoppingBasket class tests. """
    def test_shopping_basket_is_empty(self):
        shopping_basket = ShoppingBasket()
        self.assertEqual(len(shopping_basket.items), 0)

    def test_check_single_item_is_in_shopping_basket(self):
        shopping_basket = ShoppingBasket()
        shopping_basket.items.append(Item('book', 12.49, 1))
        self.assertIn(Item('book', 12.49, 1), shopping_basket.items)

    def test_check_items_are_in_shopping_basket(self):
        shopping_basket = ShoppingBasket()
        shopping_basket.items.append(Item('book', 12.49, 1))
        shopping_basket.items.append(Item('music CD', 16.49, 1))

        self.assertIn(Item('book', 12.49, 1), shopping_basket.items)
        self.assertIn(Item('music CD', 16.49, 1), shopping_basket.items)


if __name__ == '__main__':
    unittest.main()
