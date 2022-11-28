class Vehicle:
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers):
        self.brand = brand
        self.model = model
        self.engine_vol = engine_vol
        self.max_speed = max_speed
        self.total_km = total_km
        self.max_passengers = max_passengers

    def print_info(self):
        print(f"Vehicle:({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km},"
              f" {self.max_passengers})")


class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, price, sidecar):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers)
        self.price = price
        self.sidecar = sidecar

    def print_info(self):
        print(f"Vehicle:({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}"
              f", {self.price}, {self.sidecar})")


class Car(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, category, fuel):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers)
        self.category = category
        self.fuel = fuel

    def print_info(self):
        print(f"Vehicle:({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}"
              f", {self.category}, {self.fuel})")


class Bus(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, firm, year_of_manifacture):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers)
        self.year_of_manifacture = year_of_manifacture
        self.firm = firm

    def print_info(self):
        print(f"Vehicle:({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}"
              f", {self.max_passengers}, {self.firm}, {self.year_of_manifacture})")


vehicle = []


BMW = Vehicle("BMW", "E90", 3.5, 250.0, 169961.5, 4)
Kawasaki = Motorbike("Kawasaki", "Ninja", 1.0, 330.0, 29123.3, 2, 65000.2, False)
VW = Car("VW", "Golf MK3", 1.9, 320.0, 568874.6, 4, "hatchback", "diesel")
Setra = Bus("Setra", "S 519 HD", 10.7, 120.0, 999999.9, 63, "Valeros", 2015)
Audi = Vehicle("Audi", "A3", 2.0, 210.0, 160061.5, 4)
Yamaha = Motorbike("Yamaha", "R6", 0.6, 230.0, 3512623, 2, 30000.9, False)
Mazda = Vehicle("Mazda", "3", 1.6, 150.0, 369961.5, 4)
Opel = Car("Opel", "Astra H", 1.9, 350.0, 68874.6, 4, "hatchback", "diesel")
Honda = Motorbike("Honda", "CBR 125", 0.125, 130.0, 20153.6, 2, 6000.7, False)
Mercedes = Car("Mercedes-Benz", "C 63 AMG", 6.3, 340.0, 28874.6, 4, "coupe", "diesel")

BMW.print_info()
Kawasaki.print_info()
VW.print_info()
Setra.print_info()
Audi.print_info()
Mazda.print_info()
Honda.print_info()
Yamaha.print_info()
Opel.print_info()
Mercedes.print_info()

vehicle.append(BMW)
vehicle.append(Kawasaki)
vehicle.append(VW)
vehicle.append(Setra)
vehicle.append(Audi)
vehicle.append(Mazda)
vehicle.append(Honda)
vehicle.append(Yamaha)
vehicle.append(Opel)
vehicle.append(Mercedes)

print(vehicle)
