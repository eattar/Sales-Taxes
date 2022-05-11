import unittest
from shopping_basket import ShoppingBasket


class TestShoppingBasket(unittest.TestCase):
    """ ShoppingBasket class tests. """
    def test_shopping_basket_is_empty(self):
        shopping_basket = ShoppingBasket()


if __name__ == '__main__':
    unittest.main()
