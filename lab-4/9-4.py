set_1 = {2, 3, 4}
set_2 = {1, 2, 3, 4, 5}

if set_1.intersection(set_2):
    set_3 = set_2 - set_1
    print(set_3)
elif set_1.difference(set_2):
    set_4 = set_1 | set_2
    print(set_4)
