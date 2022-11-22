side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))


def is_valid_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return "Valid triangle"
    else:
        return "Invalid triangle"


can_triangle_exist = is_valid_triangle
print(can_triangle_exist(side_a, side_b, side_c))
