import sqlite3


def connect():
    conn = sqlite3.connect(food_db, timeout=None, isolation_level=None,
                           detect_types=None, factory=None)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE if NOT EXISTS food_tbl (
                                    id INTEGER,
                                    Food_name TEXT,
                                    Fat INTEGER,
                                    Protein INTEGER,
                                    Carbs INTEGER,
                                    Calories INTEGER,
                                    )""")
    conn.commit()
    conn.close()


class food:
    def __init__(self, food_name, food_fat, food_protein, food_carbs):
        self.food_name = food_name
        self.food_fat = food_fat
        self.food_protein = food_protein
        self.food_carbs = food_carbs

    def food_calories(self):
        food_calories = 9*self.food_fat + 4*(self.food_protein+self.food_carbs)
        return food_calories


def food_input():
    food_name = input("Please enter the food's name:")
    food_fat = input("Please enter it's fat value:")
    food_protein = input("Please enter it's protein value:")
    food_carbs = input("Please enter it's carbihydrate value:")


food_1 = food("chicken breast", 2, 21, 0)
print(food_1.food_name, food_1.food_calories())
