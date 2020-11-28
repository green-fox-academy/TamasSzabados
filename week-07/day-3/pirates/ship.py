from pirate import Pirate

class Ship:
    def __init__(self, name):
        self.name = name
        self.crew = []
        self.captain = None
        self.alive_crew = 0
        

    def fillShip(self, captain, pirate):
        self.captain = captain
        for i in range(random.randint(1, len(pirate))):
            self.crew.append(pirate[i])
            if pirate[i].alive == True:
                self.crew +=1

        return self.captain, self.crew

    def __str__(self):
        return 'Captain(name='+ captain.name+', rum drinked='+str(captain.count)+'captain is alive'
        + str(captain.alive) + 'alive pirates in the crew' + str(self.alive_crew) + ')'

    def battle(self, other_ship):
        ship1_score = self.alive_crew - self.captin.count/4
        ship2_score = other_ship.alive_crew -other_ship.captin.count/4
        if ship1_score > ship2_score:
            return True
        

   
#calculate score: Number of Alive pirates in the crew - Number of consumed rum by the captain
#The loser crew has a random number of losses (deaths).
#The winner captain and crew has a party, including a random number of rum :)

        
    

