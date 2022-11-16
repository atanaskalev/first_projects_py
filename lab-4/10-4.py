number = int(input("Enter number:"))
dict_1 = {}

for i in range(0, number):
    key = input("Enter key:")
    value = input("Enter value:")
    dict_1[key] = value

m = int(input("Enter another number:"))
list_1 = []

for i in range(0, m):
    value = input("Enter value:")
    list_1.append(value)

print(dict_1)
print(list_1)

for i in range(0, m):
    for key in dict_1:
        if list_1[i] == key:
            list_1[i] = dict_1[key]

print(list_1)
