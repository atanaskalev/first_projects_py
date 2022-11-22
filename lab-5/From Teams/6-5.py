lst_1 = []


def list_avg(lst):
    lst_2 = []
    el_count = int(input("Input element's count: "))
    sum_1 = 0
    for i in range(0, el_count):
        num_1 = input(f"Input element {i+1}: ")
        lst.append(num_1)
        if num_1.isnumeric() or num_1.isdigit():
            lst_2.append(num_1)
            sum_1 += float(num_1)
        avrg_1 = sum_1 / len(lst_2)
    print(lst_2)
    return avrg_1


print(list_avg(lst_1))
