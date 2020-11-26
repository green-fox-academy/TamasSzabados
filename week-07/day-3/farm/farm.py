from animals import Animal

class Farm():
    def __init__(self):
        self.animals = []
        self.slots = 100

    def add(self, animal):
        self.animals.append(animal)
        return self.animals

    def breed(self):
        if len(self.animals) < self.slots:
            animal = Animal()
            self.add(animal)


    def slaughter(self):
        hunger = 0
        least_hungry = None
        for i in self.animals:
            if i.get_hunger() > hunger:
                least_hungry = i
                hunger = i.get_hunger()

        for i in self.animals:
            if i == least_hungry:
                self.animals.remove(i)

    def get_animals(self):
        return self.animals


    
# breed() -> creates a new animal if there's place for it
# slaughter() -> removes the least hungry animal