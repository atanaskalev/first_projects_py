num_count = int(input("Enter number:"))


def input_nums(n):
    list_1 = []
    for i in range(n):
        num = input(f"Input element {i+1}:")
        if num.isnumeric():
            list_1.append(num)
    return list_1


print(input_nums(num_count))
