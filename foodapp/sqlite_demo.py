from fooditem import FoodItem

import sqlite3

conn = sqlite3.connect('fooditem.db')

#oats = FoodItem('oats', 40, 'g', 150, 27, 3, 5, 4, 1)

c = conn.cursor()

c.execute("""CREATE TABLE fooditems (
            name text,
            ss integer,
            unit text,
            cal integer,
            carb integer,
            fat integer,
            protein integer,
            fiber integer,
            sugar integer
            )""")

#c.execute("INSERT INTO fooditems VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          #pb.get_tuple())

#c.execute("INSERT INTO fooditems VALUES(:name, :ss, :unit, :cal, :carb, :fat, :protein, :fiber, :sugar)", whey.get_dict)

#c.execute("INSERT INTO fooditems VALUES('oats', 40, 'g', 150, 27, 3, 5, 4, 1)")





#c.execute("SELECT * FROM fooditems WHERE name=? OR name=? OR name=?", ('oats', 'egg', 'peanut butter'))

c.execute("SELECT * FROM fooditems WHERE name=:name", {'name': 'oats'})

print(type(c.fetchall()))

conn.commit()

conn.close()

