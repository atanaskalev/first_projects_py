# Задачата не е завършена защото ме затрудни и времето не ми стигна за да начеля начин по който да работи

from entities import Character
from entities import Item
from entities import Weapon
import Errors

characters = []
character_class = ["Warrior", "Mage", "Priest", "Rogue"]


class Menu:
    def print_menu(self):
        print("1. Create a new character")
        print("2. Create a weapon")
        print("3. Create a item")
        print("4. Print all characters")
        print("5. Delete an existing character")
        print("6. Exit")

    def command_create_character(self, name, sex, ch_class, weapon=None, item=None):
        return Character(name, sex, ch_class, weapon, item)

    def command_create_item(self, name, durability=100):
        return Item(name, durability)

    def command_create_wapon(self, name, durability, attack):
        return Weapon(name, durability, attack)

    def run(self):
        while True:
            Menu.print_menu(self)
            choice = input("Choose an item from the menu: \n> ")
            try:
                if choice == "1":
                    name_1 = input("Enter the character name (alpha-numeric): ")
                    if len(name_1) < 4:
                        raise Errors.InvalidDataFormat
                    for i in characters:
                        if i.name == name_1:
                            raise Errors.CharacterExist
                    sex = input("Enter the character sex (alpha): ")
                    if len(sex) < 4:
                        raise Errors.InvalidDataFormat
                    elif not sex.isalpha():
                        raise Errors.InvalidDataFormat
                    char_class = input("Enter the character class (Warrior, Mage, Priest, Rogue): ")
                    if len(char_class) < 4:
                        raise Errors.InvalidDataFormat
                    elif char_class is not "Warrior" or "Mage" or "Priest" or "Rogue":
                        raise Errors.InvalidCharacterClass

                    char = self.command_create_character
                    characters.append(char)

                elif choice == "2":
                    pass
                elif choice == "3":
                    pass
                elif choice == "4":
                    pass
                elif choice == "5":
                    pass
                elif choice == "6":
                    pass
                else:
                    raise Errors.InvalidCommand
            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '__main__':
    menu = Menu()
    menu.run()