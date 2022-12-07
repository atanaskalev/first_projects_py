try:
    file_1 = open("text.txt", "r")
except FileNotFoundError:
    print("File not exist")
else:
    print(str(file_1.read()))
    file_1.close()
