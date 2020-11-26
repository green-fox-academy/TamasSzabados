from sharpie import Sharpie

class Sharpie_set():
    def __init__(self):
        self.sharpies = []

    def add(self, sharpie):
        self.sharpies.append(sharpie)

    def count_usable(self):
        counter = 0
        for i in self.sharpies:
            if i.get_ink() > 0:
                counter +=1
        return counter
                

    def remove_trash(self):
        for i in self.sharpies:
            if i.get_ink() <= 0:
                self.sharpies.remove(i)
                return self.sharpies

    def get_sharpies(self):
        return self.sharpies

        


