import sqlite3


class user:
    def __init__(self, usr_name="", email="", usr_age, usr_height, usr_activity_level):
        self.usr_name = usr_name
        self.age = usr_age
        self.height = usr_height
        self.activity_level = usr_activity_level

        def bmr(self):
            bmr = self.age*1 + self.height*2 + self.activity_level*3
            return bmr
