import sqlite3


class food:
    def __init__(self, food_name, food_fat, food_protein, food_carbs):
        self.food_name = food_name
        self.food_fat = food_fat
        self.food_protein = food_protein
        self.food_carbs = food_carbs

    def food_calories(self):
        self.food_calories = 9*self.food_fat + 4*(self.food_protein+self.food_carbs)
        return self.food_calories


food_1 = food("chicken breast", 2, 21, 0)
print(food_1.food_name, food_1.food_calories() )
