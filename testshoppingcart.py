import unittest
from shoppingcart import shoppingcart

class testshoppingcart(unittest.TestCase):
    def test_add_item(self):
        cart = shoppingcart()
        cart.add_item("apple", 1.0)
        self.assertEqual(cart.get_total(), 1.0)

    def test_remove_item(self):
        cart = shoppingcart()
        cart.add_item("apple", 1.0)
        cart.remove_item("apple")
        self.assertEqual(cart.get_total(), 0.0)

if _name_ == '_main_':
    unittest.main()