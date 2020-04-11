from fooditem import FoodItem
from dao import DAO


# TODO: extract methods so that this module doesn't have TUI and logic in one place
# i.e. TUI should be in the TUI module

def calc_macros():
    food_dao = DAO()
    name = input("Enter name of food: ")
    if name == 'x':
        return None
    food_by_name = food_dao.get_foods_by_name(name)
    if food_by_name is None:
        print("No foods found")
        return None
    else:
        size = input("Enter amount: ")
        if size == 'x':
            return None
        ratio = float(size) / food_by_name.ss()
        print(f"ratio: {ratio}") # testing
        altered_food = FoodItem()
        altered_food.set_info_from_tuple(food_by_name.get_tuple())
        altered_food.proportionalize(ratio)
        return altered_food




def calc_macros(food_item, amount):
    proportioned_food = food_item.proportionalize(amount)
    return proportioned_food

















