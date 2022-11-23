num_1 = input("Enter number: ")


def digitize(num):
    tup_1 = ()
    for i in num:
        a = int(i)
        tup_1 += (a,)
    return tup_1


print(digitize(num_1))
