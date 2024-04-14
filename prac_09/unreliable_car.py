import random
from car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0