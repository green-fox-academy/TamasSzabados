from ship import Ship
class Armada:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)
        return ships 

    def armada_war(self, armada):
        i, j = 0
        while i < len(self.ships) and j < len(armada.ships):
            if self.ship.battle(armada.ships[i]) == True:
                armada.remove(armada.ships[i])
                j += 1
                
            else:
                self.ships.remove(self.ships[i])
                i += 1
            
 




