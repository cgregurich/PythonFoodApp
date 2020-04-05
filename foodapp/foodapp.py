from fooditem import FoodItem
from dao import DAO
from macros import calc_macros
import text_user_interface as tui


tui.run()

food_dao = DAO()

unsorted_foods = food_dao.get_all_foods()
sorted_foods = food_dao.sort_foods('name', 'ASC')

#tui.view_all(sorted_foods)



# LEFT OFF ON SORTING. SORTING METHODS IN DAO DO NOT WORK. FIX!!!






















