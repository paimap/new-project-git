class Vehicle:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def moving(self):
        print(f"{self.brand}\nModel: {self.model}\nis moving")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

if __name__ == "__main__":
    mobil = Car("tamiya", "avanza")
    sepeda = Bike("BMX", "sepeda terbang")

    mobil.moving()
    print("\n")
    sepeda.moving()


