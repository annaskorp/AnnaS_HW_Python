# Площадь квадрата

import math

def square(number):
    return math.ceil(number * number)
num_number = int(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {square(num_number)}")