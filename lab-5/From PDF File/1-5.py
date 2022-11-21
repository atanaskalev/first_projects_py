fig = input("Enter fig: ")


def square_1(side_a):
    s = side_a ** 2
    return s


def rectangle(side_a, side_b):
    s = (side_a * side_b)
    return s


def r_triangle(side_a, side_b):
    s = (side_a * side_b) / 2
    return s


if fig == "square":
    a = float(input("a= "))
    print(square_1(a))
elif fig == "rectangle":
    a = float(input("a= "))
    b = float(input("b= "))
    print(rectangle(a, b))
elif fig == "rectangular triangle":
    a = float(input("a= "))
    b = float(input("b= "))
    print(r_triangle(a, b))
else:
    print("Wrong figure")
