#!/usr/bin/python3
""" Get age of a person """
from datetime import date
class Person:
    def __init__(self, name, country, DOB):
        self.name = name
        self.country = country
        self.birthdate = DOB
    def get_age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        if today < date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
person_1 = Person("Edward", "Kenya", date(1991, 1, 27))
person_2 = Person("Rose", "Canada", date(1997, 12, 5))
person_3 = Person("Tiphany", "Malaysia", date(2018, 4, 17))
person_4 = Person("Debbie", "America", date(2022, 3, 12))
print("Edward:", person_1.get_age())
print("Rose:", person_2.get_age())
print("Tiphany:", person_3.get_age())
print("Debbie:", person_4.get_age())
