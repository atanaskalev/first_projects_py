a = int(input("Enter your number:"))
b = int(input("Enter your bit:"))

if a & (1 << b) > 0:
    print("True")
else:
    print("False")