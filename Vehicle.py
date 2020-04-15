class Vehicle:

    FUEL_PER_DIST = None

    def __init__(self, init_fuel):
        self.fuel = init_fuel
        self.total_distance = 0

    def move(self, distance):
        self.total_distance += distance
        self.fuel -= self.FUEL_PER_DIST * distance

    def add_fuel(self, amount):
        self.fuel += amount


class Car(Vehicle):

    FUEL_PER_DIST = 1

    def __init__(self, init_fuel):
        super().__init__(init_fuel)


if __name__ == '__main__':
    c = Car(29)
    print(c.fuel)
    c.move(10)
    print(c.fuel)



