class InvalidCommand(Exception):
    def __init__(self):
        print("Invalid command")


class InvalidDataFormat(Exception):
    def __init__(self):
        print("Invalid data format")


class CharacterExist(Exception):
    def __init__(self):
        print("Character exist")


class InvalidCharacterClass(Exception):
    def __init__(self):
        print("Invalid character class")


class CharacterNotFound(Exception):
    def __init__(self):
        print("Character not found")
