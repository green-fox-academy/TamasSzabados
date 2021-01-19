import random
from pirate import Pirate

class Ship():
    def __init__(self):
        self.pirates = []
        self.captain = None

    def fill_ship(self):
        if self.captain == None:
            captain = Pirate()
            self.captain = captain
        for i in range(1, random.randint(3,10)):
            pirate = Pirate()
            self.pirates.append(pirate)

    def info(self):
        count_alive = 0
        captain_alive = ""
        for i in self.pirates:
            if i.alive:
                count_alive += 1
        if self.captain.alive:
            captain_alive = "is alive"
        else:
            captain_alive = "has died"
        return count_alive, captain_alive

    def __repr__(self):
        return f"The captain consumed {self.captain.intoxicated} rum, and he {self.info()[1]} the number of alive pirates in the crew is {self.info()[0]}"

    def battle(self, ship):
        score = self.info()[0] - self.captain.intoxicated
        enemy = ship.info()[0] - ship.captain.intoxicated

        if score > enemy:
            for i in range(random.randint(0,len(ship.pirates))):
                ship.pirates[i].die()
            for i in range(random.randint(0, len(self.pirates))):
                self.pirates[i].drink_some_rum()
            return True

        else:
            for i in range(random.randint(0,len(self.pirates))):
                self.pirates[i].die()
            for i in range(random.randint(0, len(ship.pirates))):
                ship.pirates[i].drink_some_rum()
            return False



