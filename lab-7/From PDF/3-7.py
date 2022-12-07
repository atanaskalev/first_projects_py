import math


class WrongNumber(Exception):
    def __init__(self):
        super()


def check_positive_number(number_1):
    if number_1.isdigit() > 0 and number_1.isdigit():
        print(round(math.sqrt(int(number_1))))
    else:
        raise WrongNumber


number_2 = input("Enter number:")

try:
    check_positive_number(number_2)
except WrongNumber:
    print("Invalid number")

finally:
    print("Good Bye")
