class InvalidParameterError(Exception):
    def __init__(self):
        super()


class NutrientError(Exception):
    def __init__(self):
        super()


class InvalidFoodError(Exception):
    def __init__(self):
        super()


class Food:
    def __init__(self, carbs, protein, fats, salt):
        self.carbs = carbs
        self.protein = protein
        self.fats = fats
        self.salt = salt

        if type(self.carbs) is not float:
            raise InvalidParameterError
        if type(self.protein) is not float:
            raise InvalidParameterError
        if type(self.fats) is not float:
            raise InvalidParameterError
        if type(self.salt) is not float:
            raise InvalidParameterError
        if self.carbs + self.protein + self.fats + self.salt > 100:
            raise NutrientError
        if self.carbs == 0 and self.protein == 0 and self.fats == 0 and self.salt == 0:
            raise InvalidFoodError

    def print_label(self):
        print(f"Food({self.carbs}, {self.protein}, {self.fats}, {self.salt})")


for i in range(0, 120, 10):
    try:
        a = Food(float(i), float(i), float(i), float(i))
        a.print_label()
    except InvalidFoodError:
        print("Invalid food")
    except InvalidParameterError:
        print("Invalid parameter")
    except NutrientError:
        print("Nutrition error")
