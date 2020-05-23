import sqlite3


class food:
    def __init__(self, fat, protein, carbs):
        self.fat = fat
        self.protein = protein
        self.carbs = carbs

        def calories(self):
            calories = self.fat*9+4*(self.protein+self.carbs)
            return calories
