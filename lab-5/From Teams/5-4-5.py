def input_nums(n):
    list_1 = []
    for i in range(n):
        num = input(f"Input element {i+1}:")
        if num.isnumeric():
            list_1.append(num)
    return list_1


def sum_list(lst):
    result = 0
    for i in lst:
        if type(i) == int:
            result += i
        elif type(i) == float:
            result += i
        elif i.isnumeric():
            i = float(i)
            result += i
    return result


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


print(max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3))))
