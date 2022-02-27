class Collection:
    def __init__(self):
        self.cars = []

    def add(self, car):
        self.cars.append(car)

    def show(self):
        [print(car) for car in self.cars]

    def delete(self, car):
        self.cars.remove(car)