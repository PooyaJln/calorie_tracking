import sqlite3


class user:
    def __init__(self,  usr_name, usr_gender, usr_age, usr_height, usr_weight, usr_activity_level=0, usr_fat=0):
        self.usr_name = usr_name
        self.usr_gender = usr_gender
        self.age = usr_age  # years
        self.usr_weight = usr_weight  # kg
        self.height = usr_height  # centimeters
        self.activity_level = usr_activity_level
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
            bmr _mif = 10 + 6.25*self.usr_height-5*self.usr_age + s
            return bmr_mif


user_1 = user("Pooya", "male", 36, 181, 83)
print(user_1.usr_name,  user_1.usr_gender, user_1.usr_weight, user_1.bmr_kmca())
