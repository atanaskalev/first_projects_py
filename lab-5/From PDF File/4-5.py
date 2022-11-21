list_1 = [7, 10, 4, 2, 5, 8, 3, 6, 1, 9]
num_1 = 6


def funct_1(list_2, num_2):
    for i in range(0, list_2[-1] + 1):
        if list_2[i] > num_2:
            list_2[i] = 0
    return list_2


print(funct_1(list_1, num_1))
