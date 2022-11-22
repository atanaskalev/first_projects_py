num_1 = input("Enter number 1:")
num_2 = input("Enter number 2:")


def max_of_two(a, b):
    if a == str(a) and b != str(b):
        return b
    elif b == str(b) and a != str(a):
        return a
    elif a == str(a) and b == str(b):
        return
    elif a > b:
        return a
    elif a < b:
        return b
    elif a == b:
        return a


print(max_of_two(num_1, num_2))
