class Character:
    def __init__(self, name, sex, game_class, weapon, item):
        self.name = name
        self.sex = sex
        self.game_class = game_class
        self.weapon = weapon
        self.item = item

    def print(self):
        return str(f"{self.name}, {self.sex}, {self.game_class}, {self.weapon.print()}, {self.item.print()}")


class Item:
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability

    def print(self):
        return str(f"{self.name}, {self.durability}")


class Weapon(Item):
    def __init__(self, name, durability, attack):
        super().__init__(name, durability)
        self.attack = attack

    def print(self):
        return str(f"{self.name}, {self.durability}, {self.attack}")
