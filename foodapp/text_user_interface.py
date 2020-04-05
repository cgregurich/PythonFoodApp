from fooditem import FoodItem
from dao import DAO
import macros



food_dao = DAO()




def run():
    display_menu()
    while True:
        foo = main_menu()
        if foo is None:
            return


def main_menu():
    command = (input("\nEnter command: ")).lower()
    if command == 'x' or command == 'exit':
        return None

    elif command == 'view':
        view_all()

    elif command == 'calc':
        calc_macros()

    elif command == 'add':
        add_new_food()

    elif command == 'del':
        del_food()

    elif command == 'update':
        update_food()

    elif command == 'sort':
        sort()

    elif command == 'help':
        display_menu()

    else:
        print("Invalid command.")
        return main_menu()
    return 0


def display_menu():
    print("\nCOMMANDS - Enter a command (not case sensitive)")
    print("(Enter x at any time to quit)")  # todo, this doesn't work fully; no x clause in functions
    print("VIEW - View all foods")
    print("CALC - Calculate macros for a given food based on an amount")
    print("ADD - Add a new food")
    print("DEL - Delete a food by name")
    print("UPDATE - Update a food by name")
    print("SORT - Sort foods")
    print("HELP - Display these options")
    print("EXIT - Quit the program")

def get_header_len():
    div = 0
    all_foods = food_dao.get_all_foods()
    for food in all_foods:
        if len(food.name()) > div:
            div = len(food.name())
    div += 2
    if div < 9:
        div = 9
    return div


def view_all(foods_list=None):
    """takes care of displaying the table of foods in a formatted way"""
    div = get_header_len()
    print_heading(div)

    if foods_list is None:
        foods = food_dao.get_all_foods()
        for food in foods:
            print(food.str_formatted(div))
    else:
        for food in foods_list:
            print(food.str_formatted(div))



def print_heading(div):
    """prints the heading for the table"""
    div = div  # space each heading takes up
    headings = ['name', 'ss', 'unit', 'cal', 'carb', 'fat', 'protein', 'fiber', 'sugar']
    line1 = ''
    for heading in headings:
        space_count = div - len(heading)
        spaces = ' ' * space_count
        line1 += f"{heading.upper()}{spaces}"
    line2 = '-' * len(line1)
    print(line1)
    print(line2)

def calc_macros():
    altered_food = macros.calc_macros()
    if altered_food is None or altered_food == 'x':
        return None
    div = len(altered_food.name()) + 2
    if div < 9:
        div = 9
    print_heading(div)
    print(altered_food.str_formatted(div))

def add_new_food():
    print('\nADDING NEW FOOD')
    new_info = get_food_info()
    if new_info is None:
        return False
    insert_food(new_info)
    print("Food was added!")
    return True


def get_food_info():
    prompts = ('name', 'ss', 'unit', 'cal', 'carb', 'fat', 'protein', 'fiber', 'sugar')
    info = []
    answer = ''
    i = 0
    while answer != 'x' and i < 9:
        answer = input(f"Enter {prompts[i]}: ")
        if answer == 'x':
            return None
        if prompts[i] == 'name':
            foods_with_name = food_dao.get_foods_by_name(answer)
            if foods_with_name is not None: # exists
                print(f"\nFood with name '{answer}' already exists")
                return None
        info.append(answer)
        i += 1
    return info


def insert_food(food_info):
    food = FoodItem()
    food.set_info_from_list(food_info)
    food_dao.insert_food(food)


def del_food():
    name = get_name_to_del()


def get_name_to_del():
    name = input("Enter name of food to delete: ")
    remove_food(name)
    return name


def remove_food(name):
    if name == 'x':
        return False
    rows_affected = food_dao.remove_food(name)
    if rows_affected >= 1:
        print(f"{name} was removed")
    else:
        print(f"{name} doesn't exist")


def update_food():
    updated_food = get_update_info()
    if updated_food is None:
        return None
    food_dao.update_info(updated_food)


def get_update_info():
    prompts = ('name', 'ss', 'unit', 'cal', 'carb', 'fat', 'protein', 'fiber', 'sugar')
    info = []
    updated_food = FoodItem()
    answer = ''
    i = 0
    while answer != 'x' and i < 9:
        answer = input(f"Enter {prompts[i]}: ")
        if answer.lower() == 'x':
            return None
        if prompts[i] == 'name':
            food_by_name = food_dao.get_foods_by_name(answer)
            if food_by_name is None:
                print(f"\nNo results found for {answer}")
                return None
        info.append(answer)
        i += 1
    updated_food.set_info_from_list(info)
    return updated_food

def sort():
    a = ''
    while True:
        print("\nSort by what?")
        a = input("(name, ss, unit, cal, carb, fat, protein, fiber, sugar): ")
        if a.lower() == 'x':
            return None
        elif a.lower() == 'name' or a == 'ss' or a == 'unit' or a == 'cal' or a == 'carb' or a == 'fat' or a == 'protein' or a == 'fiber' or a == 'sugar':
            break
        else:
            print("\nInvalid input.")
    o = ''
    while True:
        print("\nAscending or descending?")
        o = (input(("(asc or desc): "))).lower()
        if o == 'x':
            return None
        elif o == 'asc' or o == 'desc':
            break
        else:
            print("\nInvalid input.")
    sorted_foods = food_dao.sort_foods(a, o)
    view_all(sorted_foods)






