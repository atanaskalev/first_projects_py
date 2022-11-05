a = 27101022
b = 2
c = ""
while a > 0:
    c += str(a % 2)
    a //=2
print(c[::-1])
