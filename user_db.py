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
    def __init__(self,  u_name, u_gender, u_age, u_height, u_weight, u_activity_level=0, u_fat=0):
        self.u_name = u_name
        self.u_gender = u_gender
        self.u_age = u_age  # years
        self.u_weight = u_weight  # kg
        self.u_height = u_height  # centimeters
        self.u_activity_level = u_activity_level
        self.u_fat = u_fat  # body fat percentage

    def bmr_kmca(self):
        # Katch-McArdle formula
        lmb = self.u_weight*(1-self.u_fat/100)
        bmr_kmca = 370 + 21.6*lmb
        return bmr_kmca

    def bmr_mif(self):
        # The Mifflin St Jeor Equation formula
        if self.u_gender == "male":
            s = 5
        else:
            s = -161
        bmr_mif = 10 + 6.25*self.u_height-5*self.u_age + s
        return bmr_mif

    def u_food_db_name(self):
        self.u_food_db_name = self.u_name + "_food_db.db"
        return self.u_food_db_name


def user_input():
    u_name = input("What do you want me to call you? ")
    u_gender = input("Please enter your gender: ")
    u_age = input("You look young but may I ask how old you are? ")
    u_height = input("How tall are you in centeimeters? ")
    u_weight = input("How much that stupid scale says you weigh in kg? ")
    u_fat = input("Optional! Please enter your body fat percentage:")


user_1 = user("Pooya", "male", 36, 181, 83, u_fat=18)
print(user_1.u_name,  user_1.u_fat, user_1.u_food_db_name(),
      user_1.bmr_mif(), user_1.bmr_kmca())
print user_1
