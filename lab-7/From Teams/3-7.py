import random


class InvalidParameterError(Exception):
    def __init__(self, name=""):
        super()
        self.name = name
        print(f"Invalid class Parameter: {self.name}")


class InvalidAgeError(InvalidParameterError):
    def __init__(self, age):
        super()
        self.age = age
        print(f"Invalid class Parameter: {self.age}")


class InvalidSoundError(InvalidParameterError):
    def __init__(self, sound):
        super()
        self.sound = sound
        print(f"Invalid class Parameter: {self.sound}")


class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        if type(name) is not str:
            raise InvalidParameterError(name)
        if type(age) is not int:
            raise InvalidAgeError(age)
        if type(sound) is not str:
            raise InvalidSoundError(sound)

    def make_sound(self):
        return f"{self.name} says {self.sound}!"

    def print(self):
        pass

    def daily_task(self, *args):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError(age)
        if sound.count("r") <= 2:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for i in animals:
            if type(i).__name__ == Lemur or type(i).__name__ == Human:
                print(f"{self.name} the Jaguar hunted down {i.name} the {type(i).__name__}")
                del animals[i]


class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError(age)
        if sound.count("e") == 0:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_task(self, fruits):
        if fruits >= 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            fruits -= 10
            return fruits
        if fruits < 10:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
        if fruits <= 0:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            fruits = 0
            return fruits


class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError(age)
        if sound.count("e") == 0:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals, buildings):
        a = False
        for i in animals:
            if type(i).__name__ == Human:
                if i == 0:
                    if type(i + 1).__name__ == Human:
                        a = True
                elif i == len(animals - 1):
                    if type(i - 1).__name__ == Human:
                        a = True
                elif 0 > i > len(animals - 1):
                    if type(i + 1).__name__ == Human and type(i - 1).__name__ == Human:
                        a = True
                if a is True:
                    buildings.append(Building("Blok"))


class Building:
    def __init__(self, type_1):
        self.type_1 = type_1


fruits = 100
animals = []
buildings = []

names = ["Jacob", "David", "Bobby", "Steve", "Johanssen", "Mac", "Jason", "Edward", "Alex", "Maddie", "Susan",
         "Abigail", "Jessica", "Lizzy", "Monica", "Lorelei", "Sandra", "Michelle"]

sounds = ["RAAWR", "ROAR", "Grrr", "Shriek", "Meow", "Eeek", "Aaaaa", "Speak", "I am a Human"]

for i in range(102):
    name_1 = names[random.randrange(len(names))]
    sound_1 = sounds[random.randrange(len(sounds))]
    age_1 = random.randint(7, 20)
    a = random.randint(0, 9)
    try:
        if 0 <= a <= 3:
            animals.append(Lemur(name_1, age_1, sound_1))
        elif 4 <= a <= 7:
            animals.append(Jaguar(name_1, age_1, sound_1))
        else:
            animals.append(Human(name_1, age_1, sound_1))
    except InvalidAgeError:
        print(InvalidAgeError)
    except InvalidSoundError:
        print(InvalidSoundError)


print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim).__name__ == Jaguar:
        anim.daily_task(animals)
    if type(anim).__name__ == Lemur:
        anim.daily_task(fruits)
    if type(anim).__name__ == Human:
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
