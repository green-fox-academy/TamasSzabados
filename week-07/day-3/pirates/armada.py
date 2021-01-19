from ship import Ship

class Armada():
    def __init__(self):
        self.ships = []

    def add_ship(self,ship):
        self.ships.append(ship)

    def armada_war(self, armada):
        i = 0
        j = 0
        while i < len(self.ships) and j < len(armada.ships):
            if self.ships[i].battle(armada.ships[i]) == True:
                armada.remove(armada.ships[i])
                j += 1
            else:
                self.ships.remove(self.ships[i])
                i += 1
        if i < len(self.ships) and j == len(armada.ships):
            return True


