class Meal:
    def __init__(self):
        self.ingredients_list = []

    def add_ingredient(self, food_item, amount):
        ingredient_dict = {'food_item': food_item, 'amount': amount}
        meal_ing = food_item.proportionalize(amount)
        print(food_item)# testing
        print(f"meal_ing: {meal_ing}")#testing
        self.ingredients_list.append(meal_ing)

    def get_ingredients(self):
        return self.ingredients_list

    def __str__(self):
        string = ''
        for ingredient in self.ingredients_list:
            #string += f"{ingredient['food_item'].name()} - {ingredient['amount']} {ingredient['food_item'].unit()}  "
            string += ingredient.str_formatted()
        return string

    def calc_meal_macros(self):
        macros_dict = {'cal': 0.0, 'carb': 0.0, 'fat': 0.0, 'protein': 0.0, 'fiber': 0.0, 'sugar': 0.0}
        for ingredient in self.ingredients_list: #dictionary
            current_food = ingredient['food_item']
            ratio = ingredient['amount'] / int(current_food.ss())
            altered_food = current_food
            altered_food.proportionalize(ratio)
            altered_info_dict = altered_food.get_dict()
            for key, value in macros_dict.items():
                macros_dict[key] += altered_info_dict[key]

        return macros_dict




