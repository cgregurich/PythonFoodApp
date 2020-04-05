from fooditem import FoodItem

import sqlite3

conn = sqlite3.connect('fooditem.db')

#oats = FoodItem('oats', 40, 'g', 150, 27, 3, 5, 4, 1)

c = conn.cursor()

#c.execute("""CREATE TABLE fooditems (
            #name text,
            #ss integer,
            #unit text,
            #cal integer,
            #carb integer,
            #fat integer,
            #protein integer,
            #fiber integer,
            #sugar integer
            #)""")

pb = FoodItem('peanut butter', 32, 'g', 190, 5, 8, 6, 2, 4)
whey = FoodItem('whey', 32, 'g', 124, 5, 2, 25, 0, 0)
#c.execute("INSERT INTO fooditems VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          #pb.get_tuple())

#c.execute("INSERT INTO fooditems VALUES(:name, :ss, :unit, :cal, :carb, :fat, :protein, :fiber, :sugar)", whey.get_dict)

#c.execute("INSERT INTO fooditems VALUES('oats', 40, 'g', 150, 27, 3, 5, 4, 1)")

print(whey.get_dict())

print('\n\n\n')




#c.execute("SELECT * FROM fooditems WHERE name=? OR name=? OR name=?", ('oats', 'egg', 'peanut butter'))

c.execute("SELECT * FROM fooditems WHERE name=:name", {'name': 'oats'})

print(type(c.fetchall()))

conn.commit()

conn.close()

