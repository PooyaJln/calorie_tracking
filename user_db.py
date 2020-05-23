import sqlite3


def connect():
    conn = sqlite3.connect("user_db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE if NOT EXISTS user_tbl (
                                    id INTEGER,
                                    Name TEXT,
                                    Gender TEXT
                                    Age INTEGER,
                                    Height INTEGER,
                                    Weight INTEGER,
                                    Body_fat INTEGER,
                                    )""")
    conn.commit()
    conn.close()


class user:
    def __init__(self,  usr_name, usr_gender, usr_age, usr_height, usr_weight, usr_activity_level=0, usr_fat=0):
        self.usr_name = usr_name
        self.usr_gender = usr_gender
        self.usr_age = usr_age  # years
        self.usr_weight = usr_weight  # kg
        self.usr_height = usr_height  # centimeters
        self.usr_activity_level = usr_activity_level
        self.usr_fat = usr_fat  # body fat percentage

    def bmr_kmca(self):
        # Katch-McArdle formula
        bmr_kmca = 370 + 216*(self.usr_weight*(1-self.usr_fat/100))
        return bmr_kmca

    def bmr_mif(self):
        # The Mifflin St Jeor Equation formula
        if self.usr_gender == "male":
            s = 5
        else:
            s = -161
        bmr_mif = 10 + 6.25*self.usr_height-5*self.usr_age + s
        return bmr_mif

    def usr_food_db_name(self):
        self.usr_food_db_name = self.usr_name + "_food_db.db"
        return self.usr_food_db_name


user_1 = user("Pooya", "male", 36, 181, 83, usr_fat=18)
print(user_1.usr_name,  user_1.usr_fat, user_1.usr_food_db_name(), user_1.bmr_mif(), user_1.bmr_kmca())
