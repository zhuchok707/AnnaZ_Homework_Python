import math


def square(side):
    result = side * side
    return math.ceil(result)


side_length = 14
print(f"Площадь квадрата со стороной {side_length} = {square(side_length)}")
