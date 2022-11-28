class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality


class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience


students = []

todor = Lecturer("Todor", "Manev", "40", "Bulgarian", "TU", "12")
pancho = Lecturer("Pancho", "Penev", "52", "Bulgarian", "PU", "23")
serafim = Lecturer("Serafim", "Rusev", "63", "Bulgarian", "SU", "34")

students.append(todor)
students.append(pancho)
students.append(serafim)
print(f"Name:{serafim.name} {serafim.family}", f"  Nationality:{serafim.nationality}",
      f"  University:{serafim.university}", f"  Year of experience:{serafim.experience}")
print(f"Name:{todor.name} {todor.family}", f"  Nationality:{todor.nationality}", f"  University:{todor.university}",
      f"  Year of experience:{todor.experience}")
print(f"Name:{pancho.name} {pancho.family}", f"  Nationality:{pancho.nationality}", f"  University:{pancho.university}",
      f"  Year of experience:{pancho.experience}")
print(students)
