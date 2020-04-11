import unittest
import sys
from foodapp import fooditem

class TestFoodItem(unittest.TestCase):
    def setup(self):
        self.food_1 = FoodItem('apple', '50', 'g', '100', '20', '1', '2', '3', '10')

    def test_set_info_from_dict(self):
        new_info = {'name': 'banana', 'ss': '30', 'unit': 'grams', 'cal': '120', 'carb': '25', 'fat': '0', 'protein': '2', 'fiber': '5', 'sugar': '20'}
        self.food_1.set_info_from_dict(new_info)
        self.assertEqual(self.food_1.name == 'banana')
        self.assertEqual(self.food_1.ss == '30')
        self.assertEqual(self.food_1.unit == 'grams')
        self.assertEqual(self.food_1.cal == '120')
        self.assertEqual(self.food_1.carb == '25')
        self.assertEqual(self.food_1.fat == '0')
        self.assertEqual(self.food_1.protein == '2')
        self.assertEqual(self.food_1.sugar == '5')
        self.assertEqual(self.food_1.fiber == '20')



if __name__ == '__main__':
    unittest.main()