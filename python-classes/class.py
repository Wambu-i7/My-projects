#!/usr/bin/python3
class CarDesign:
    def __init__(self, made, plate):
        self.company = made
        self.number = plate
        self.wheels = 4
car1 = CarDesign("Toyota", "001")
print(car1.company)
print(car1.number)
print(car1.wheels)
