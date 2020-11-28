class Pirate:
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.alive = True
        self.parrot = ""

    def drinkSomeRum(self):
        return self.count += 1
        

    def howsItGoingMate(self):
        if self.count <= 4 and self.alive == True:
            print("Pour me anudder!")
        elif self.count > 4 and self.alive == True::
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
        elif self.alive == False:
            print("he's dead")

    def die(self):
        self.alive = False

    def brawl(self, pirate):
        if pirate.alive == True:
            if random.random() < 0.33:
                self.alive = False

            elif 0.33 <= random.random() <= 0.66:
                pirate.alive = False
                self.alive = False

            elif random.random() > 0.66:
                pirate.alive = False

    def add_parrot(self, parrot):
        self.parrot = parrot


