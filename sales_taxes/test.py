import math


def round_to_value(number, base):
    return (math.ceil(number / base) * base)

print(round_to_value(6.66, 0.05))