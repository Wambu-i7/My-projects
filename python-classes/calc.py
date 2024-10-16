#!/usr/bin/python3
class Calculator:
    def __init__(self, first_digit, sec_digit):
        self.first_d = first_digit
        self.sec_d = sec_digit
    def addition(self):
        return self.first_d + self.sec_d
    def subtract(self):
        if self.first_d < self.sec_d:
            return
        else:
            return self.first_d - self.sec_d
    def multiply(self):
        return self.first_d * self.sec_d
    def division(self):
        if self.sec_d == 0:
            return ("Cannot divide by zero.")
        else:
            return self.first_d / self.sec_d
calc_1 = Calculator(12, 8)
print("Addition is:", calc_1.addition())
print("Subtraction is:", calc_1.subtract())
print("Multiplication is:", calc_1.multiply())
print("Division is:", calc_1.division())
