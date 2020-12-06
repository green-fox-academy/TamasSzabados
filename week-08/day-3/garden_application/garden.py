class Garden():
    def __init__(self):
        self.plants = []
        
    def add(self, plant):
        self.plants.append(plant)

    @property
    def get_plants(self):
        return self.plants

    def describe_garden(self):
        for i in self.plants:
            if isinstance(i, Trees):
                if i.water < 10:
                    print(f"The {i.name} {self.__class__.__name__} needs water")
                else:
                    print(f"The {i.name} {self.__class__.__name__} doesnt need water")

            if isinstance(i, Flowers):
                if i.water < 4:
                    print(f"The {i.name} {self.__class__.__name__} needs water")
                else:
                    print(f"The {i.name} {self.__class__.__name__} doesnt need water")

    def watering(self, num):
        print(f"Watering with {num}")
        equal_water = num/len(self.plants)
        for i in self.plants:
            if isinstance(i, Trees):
                if i.water < 10:
                    i.water += (equal_water * i.absorption)
            if isinstance(i, Flowers):
                if i.water < 4:
                    i.water += (equal_water * i.absorption)        
        
        self.describe_garden()


class Trees():
    absorption = 0.75
    def __init__(self,name):
        self.name = name
        self.water = 2

class Flowers(Garden):
    absorption = 0.4
    def __init__(self,name):
        self.name = name
        self.water = 3

        