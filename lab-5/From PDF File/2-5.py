num = int(input("Enter number: "))


def palindrom_1(n):
    if n == n[::-1]:
        return 1
    else:
        return 0


print(palindrom_1(str(num)))
