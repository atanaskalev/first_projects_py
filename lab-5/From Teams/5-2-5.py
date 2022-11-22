list_1 = [1, 2.5, 5, "5", "a", 8, "="]


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


print(sum_list(list_1))
