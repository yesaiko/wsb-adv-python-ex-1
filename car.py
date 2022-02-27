class Car:
    def __init__(self, make, year, mileage):
        self.make = make
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f"{ self.make } - { self.year }r - { self.mileage }km"


