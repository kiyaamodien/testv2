import unittest
from main import MyMiniCalculator

calc = MyMiniCalculator()


class TestAdd(unittest.TestCase):
    def testadd(self):
        add_method = calc.add
        self.assertEqual(add_method(1, 1), 2, 'Adding 1 and 1 should be 2')
        self.assertEqual(add_method('a', 'b'), 'ab', 'Adding a and b should be ab')
