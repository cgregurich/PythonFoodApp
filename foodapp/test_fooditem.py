import unittest
import sys
from fooditem import FoodItem

class TestFoodItem(unittest.TestCase):
    def setUp(self):
        self.food_1 = FoodItem('apple', '50', 'g', '100', '20', '1', '2', '3', '10')
        self.food_2 = FoodItem('oats', '40', 'g', '120', '25', '3', '5', '6', '1')

    def test_set_info_from_dict(self):
        new_info = {'name': 'banana', 'ss': '30', 'unit': 'grams', 'cal': '120', 'carb': '25', 'fat': '0', 'protein': '2', 'fiber': '5', 'sugar': '20'}
        self.food_1.set_info_from_dict(new_info)
        self.assertEqual('banana', self.food_1.name)
        self.assertEqual('30', self.food_1.ss)
        self.assertEqual('grams', self.food_1.unit)
        self.assertEqual('120', self.food_1.cal)
        self.assertEqual('25', self.food_1.carb)
        self.assertEqual('0', self.food_1.fat)
        self.assertEqual('2', self.food_1.protein)
        self.assertEqual('5', self.food_1.fiber)
        self.assertEqual('20', self.food_1.sugar)

    def test_proportionalize(self):
        self.food_1.proportionalize(100)

        self.assertEqual('apple', self.food_1.name)
        self.assertEqual('100.0', self.food_1.ss)
        self.assertEqual('g', self.food_1.unit)
        self.assertEqual('200.0', self.food_1.cal)
        self.assertEqual('40.0', self.food_1.carb)
        self.assertEqual('2.0', self.food_1.fat)
        self.assertEqual('4.0', self.food_1.protein)
        self.assertEqual('6.0', self.food_1.fiber)
        self.assertEqual('20.0', self.food_1.sugar)

        self.food_2.proportionalize(125)
        self.assertEqual('oats', self.food_2.name)
        self.assertEqual('125.0', self.food_2.ss)
        self.assertEqual('g', self.food_2.unit)
        self.assertEqual('375.0', self.food_2.cal)
        self.assertEqual('78.1', self.food_2.carb)
        self.assertEqual('9.4', self.food_2.fat)
        self.assertEqual('15.6', self.food_2.protein)
        self.assertEqual('18.8', self.food_2.fiber)
        self.assertEqual('3.1', self.food_2.sugar)






if __name__ == '__main__':
    unittest.main()