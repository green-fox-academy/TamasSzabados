from car import Car

class Station:
    def __init__(self):
        self.gas_amount = 5000

    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount = car.capacity
        return self.gas_amount

    