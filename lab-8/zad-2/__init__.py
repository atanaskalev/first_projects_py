from sum import summation
from sub import subtraction
from mult import multiplication
from div import division

action = input("Enter action: ")
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))

if action == "+":
    summation(a, b)

elif action == "-":
    subtraction(a, b)

elif action == "*":
    multiplication(a, b)

elif action == "/":
    if b == 0:
        raise ZeroDivisionError
    else:
        division(a, b)
