operation_1 = input("Enter +, -, *, / : ")
num_1 = int(input("Enter number 1:"))
num_2 = int(input("Enter number 2:"))


def subirane(a, b):
    result_1 = a + b
    return result_1


def izvazhdane(a, b):
    result_2 = a - b
    return result_2


def umnozhenie(a, b):
    result_3 = a * b
    return result_3


def delene(a, b):
    result_4 = a / b
    return result_4


if operation_1 == "+":
    print(subirane(num_1, num_2))
elif operation_1 == "-":
    print(izvazhdane(num_1, num_2))
elif operation_1 == "*":
    print(umnozhenie(num_1, num_2))
elif operation_1 == "/":
    print(delene(num_1, num_2))
else:
    print("Invalid operation")
