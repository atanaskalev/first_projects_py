class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality


students = []

toni = Person("Toni", "Montana", "33", "Mexican")
pesho = Person("Pesho", "Petrov", "26", "Bulgarian")
sasho = Person("Sasho", "Roman", "23", "Arabian")

students. append(toni)
students. append(pesho)
students. append(sasho)
print(f"Name:{sasho.name} {sasho.family}", f"  Nationality:{sasho.nationality}")
print(f"Name:{toni.name} {toni.family}", f"  Nationality:{toni.nationality}")
print(f"Name:{pesho.name} {pesho.family}", f"  Nationality:{pesho.nationality}")
print(students)
