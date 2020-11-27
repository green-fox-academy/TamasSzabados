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
        else:
            print("he's dead")

    def die(self):
        self.alive = False

    #brawl(x) - where pirate fights another pirate (if that other pirate is alive) and there's a 1/3 chance, 
    # 1 dies, the other dies or they both pass out.

    def add_parrot(self, parrot):
        self.parrot = parrot


