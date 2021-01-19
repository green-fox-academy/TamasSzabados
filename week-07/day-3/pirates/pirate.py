import random

class Pirate():
    def __init__(self):
        self.intoxicated = 0
        self.alive = True
        self.parrot = False

    def drink_some_rum(self):
        if self.alive:
            self.intoxicated += 1
        else:
            print("he's dead")

    def hows_it_going_mate(self):
        if self.intoxicated < 5 and self.alive:
            print("Pour me anudder!")
        elif self.intoxicated >= 5 and self.alive:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
        elif not self.alive:
            print("he's dead")

    def die(self):
        self.alive = False

    def brawl(self, pirate):
        chance = random.random()
        if pirate.alive == True:
            chance = random.random()
            if chance < 0.33:
                self.alive = False
            elif 0.33 <= chance <= 0.66:
                pirate.alive = False
                self.alive = False
            elif chance > 0.66:
                pirate.alive = False
                self.parrot()

    def parrot(self):
        self.parrot = True
    



    

