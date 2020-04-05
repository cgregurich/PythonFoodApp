from fooditem import FoodItem

import sqlite3


class DAO:
    def __init__(self):
        self.conn = sqlite3.connect('fooditem.db')
        self.c = self.conn.cursor()

    def insert_food(self, food):
        with self.conn:
            self.c.execute("INSERT INTO fooditems VALUES (:name, :ss, :unit, :cal, :carb, :fat, :protein, :fiber, :sugar)", food.get_dict())

    def get_foods_by_name(self, name):
        self.c.execute("SELECT * FROM fooditems WHERE name=?", (name,))
        food_info_tuple = self.c.fetchone()
        food = FoodItem()
        if food_info_tuple is None:
            return None
        food.set_info_from_tuple(food_info_tuple)
        return food


    def update_info(self, updated_food):
        with self.conn:
            self.c.execute("UPDATE fooditems SET name=:name, ss=:ss, unit=:unit, cal=:cal, carb=:carb, fat=:fat, "
                           "protein=:protein, fiber=:fiber, sugar=:sugar WHERE name=:name", (updated_food.get_dict()))
        return self.c.rowcount

    def remove_food(self, name):
        with self.conn:
            self.c.execute("DELETE FROM fooditems WHERE name = ?", (name,))
        return self.c.rowcount

    def get_all_foods(self):
        """returns a list of all food items in the db"""
        with self.conn:
            self.c.execute("SELECT * FROM fooditems")
            all_foods = self.c.fetchall()
        food_items = []
        for info_list in all_foods:
            food = FoodItem()
            food.set_info_from_list(info_list)
            food_items.append(food)
        return food_items

    def sort_foods(self, sort_type, order):
        with self.conn:
            self.c.execute(f"SELECT * FROM fooditems ORDER BY {sort_type} {order}")
            sorted_foods = self.c.fetchall()
        return self.convert_to_food_items_list(sorted_foods)


# THIS METHOD PROB NEEDS TO BE USED BY MORE METHODS; WILL HAVE TO REFACTOR STUFF
    def convert_to_food_items_list(self, fetched):
        foods_list = []
        for info_tuple in fetched:
            food = FoodItem()
            food.set_info_from_tuple(info_tuple)
            foods_list.append(food)
        return foods_list
