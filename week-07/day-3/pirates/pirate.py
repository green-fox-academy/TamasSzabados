class Pirate:
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.alive = True
        self.parrot = ""

    def drinkSomeRum(self):
        self.count += 1
        return self.count
        

    def howsItGoingMate(self):
        if self.count <= 4 and self.alive:
            print("Pour me anudder!")
        elif self.count > 4 and self.alive:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
        elif not self.alive:
            print("he's dead")

    def die(self):
        self.alive = False

    def brawl(self, pirate):
        if pirate.alive == True:
            chance = random.random()
            if chance < 0.33:
                self.alive = False
            elif 0.33 <= chance <= 0.66:
                pirate.alive = False
                self.alive = False
            elif chance > 0.66:
                pirate.alive = False
                
    def add_parrot(self, parrot):
        self.parrot = parrot


