class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality


class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy


students = []

toni = Student("Toni", "Montana", "33", "Mexican", "TU", "2")
pesho = Student("Pesho", "Petrov", "26", "Bulgarian", "PU", "3")
sasho = Student("Sasho", "Roman", "23", "Arabian", "SU", "4")

students.append(toni)
students.append(pesho)
students.append(sasho)
print(f"Name:{sasho.name} {sasho.family}", f"  Nationality:{sasho.nationality}", f"  University:{sasho.university}",
      f"  Year of study:{sasho.yearofstudy}")
print(f"Name:{toni.name} {toni.family}", f"  Nationality:{toni.nationality}", f"  University:{toni.university}",
      f"  Year of study:{toni.yearofstudy}")
print(f"Name:{pesho.name} {pesho.family}", f"  Nationality:{pesho.nationality}", f"  University:{pesho.university}",
      f"  Year of study:{pesho.yearofstudy}")
print(students)
