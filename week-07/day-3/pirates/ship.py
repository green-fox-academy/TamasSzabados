from pirate import Pirate
import random

class Ship:
    def __init__(self, name):
        self.name = name
        self.crew = []
        self.captain = None
      
        

    def fillShip(self, captain):
        self.captain = captain
        pirates_num = random.randint(6,10)
        for i in range(pirates_num):
            pirate = Pirate("Jack" + str(i))
            self.crew.append(pirate)
            

    def get_alive(self):
        alive_crew = 0
        for i in self.crew:
            if i.alive:
                alive_crew +=1
        return alive_crew

    def __str__(self):
        return 'Captain(name='+ captain.name+', rum drinked='+str(captain.count)+'captain is alive'
        + str(captain.alive) + 'alive pirates in the crew' + str(self.get_alive()) + ')'

    def battle(self, other_ship):
        ship1_score = self.get_alive() - self.captain.count
        ship2_score = other_ship.get_alive() - other_ship.captain.count
        if ship1_score > ship2_score:
            for i in range(random.randint(1, len(self.crew))):
                self.crew[i].drinkSomeRum()
            
            for i in range(random.randint(1, len(other_ship.crew))):
                other_ship.crew[i].die()
            print(self.name + " won the battle")
            return True
            
        else:
            for i in range(random.randint(1, len(other_ship.crew))):
                other_ship.crew[i].drinkSomeRum()
            for i in range(random.randint(1, len(self.crew))):
                self.crew[i].die()
            print(other_ship.name + " won the battle")
            return False


        



        
    

