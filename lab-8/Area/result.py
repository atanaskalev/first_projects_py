from square1 import square_area
from triangle1 import triangle_area
from rhombus1 import rhombus_area
from trapezoid1 import trapezoid_area
from rectangular1 import rectangular_area

figure = input("Enter figure: ")

if figure == "square":
    a = float(input("Enter a: "))
    square_area(a)

elif figure == "triangle":
    a = float(input("Enter a: "))
    h = float(input("Enter h: "))
    triangle_area(a, h)

elif figure == "rhombus":
    a = float(input("Enter a: "))
    h = float(input("Enter h: "))
    rhombus_area(a, h)

elif figure == "trapezoid":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    h = float(input("Enter h: "))
    trapezoid_area(a, b, h)

elif figure == "rectangular":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    rectangular_area(a, b)

else:
    print("None defining figure!!!")
