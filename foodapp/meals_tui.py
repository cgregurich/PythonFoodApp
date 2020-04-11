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


def display_menu():
    print("\nCOMMANDS - Enter a command (not case sensitive)")
    print("(Enter x at any time to quit)")  # todo, this doesn't work fully; no x clause in functions
    print("PLAN - View the meal plan")
    print("VIEW - View an individual meal")
    print("NEW - Create a new meal and add it to the plan")
    print("DEL - Delete a meal from the plan")
    print("UPDATE - Update a meal in the plan")
    print("HELP - Display these options")
    print("EXIT - Quit the program")


def main_menu():
    command = (input("\nEnter command: ")).lower()
    if command == 'x' or command == 'exit':
        return None

    elif command == 'plan':
        pass

    elif command == 'view':
        pass

    elif command == 'new':
        pass

    elif command == 'del':
        pass

    elif command == 'update':
        pass

    elif command == 'help':
        display_menu()

    else:
        print("Invalid command.")
        return main_menu()
    return 0

def new_meal():
    pass


def get_new_meal_input():
    ing_name = input("Enter ingredient name: ")

