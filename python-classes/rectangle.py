#!/usr/bin/python3
class Rectangle:
    def __init__(self, length, width):
        self.len = length
        self.wid = width
    def get_area(self):
        return self.len * self.wid
    def get_perimeter(self):
        return (2 * self.len) + (2 * self.wid)
Rect_1 = Rectangle(10, 20)
print(Rect_1.get_area())
Rect_2 = Rectangle(9, 10)
print(Rect_2.get_area())
print(f"Perimeter is {Rect_1.get_perimeter()}")
