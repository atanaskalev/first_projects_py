a = 27101022
c = ""
while a > 0:
    reminder = a % 16
    if reminder == 10:
        c += 'A'
    if reminder == 11:
        c += 'B'
    if reminder == 12:
        c += 'C'
    if reminder == 13:
        c += 'D'
    if reminder == 14:
        c += 'E'
    if reminder == 15:
        c += 'F'
    else:
     c += str(reminder)
    a //= 16
print(c[::-1])
