n = int(input("Number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Ne e prosto")
            break
    else:
        print("Prosto e")
else:
    print("Ne e prosto")