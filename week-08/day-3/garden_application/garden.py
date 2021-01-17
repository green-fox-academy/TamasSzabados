class Garden():
    def __init__(self):
        self.plants = []
        
    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant):
        self.plants.remove(plant)
    
    def water_needed(self):
        count_water = 0
        for i in self.plants:
            if isinstance(i, Flower):
                water_needed = 5 - i.water
                if water_needed > 0:
                    count_water +=1     
            else:
                water_needed = 10 - i.water
                if water_needed > 0:
                    count_water +=1
        return count_water

    def water(self,num):
        count_water = self.water_needed()
        equal_water = num / count_water
        for i in self.plants:
            if isinstance(i, Tree):
                if i.water < 10:
                    i.water += (equal_water * i.absorbing_rate)
            if isinstance(i, Flower):
                if i.water < 5:
                    i.water += (equal_water * i.absorbing_rate)
        print(f"Watering with {num}")
        self.info()

    def info(self):
        for i in self.plants:
            if isinstance(i, Tree):
                if i.water < 10:
                    print(f"The {i.color} {i.__class__.__name__} needs water")
                else:
                    print(f"The {i.color} {i.__class__.__name__} doesnt need water")

            if isinstance(i, Flower):
                if i.water < 5:
                    print(f"The {i.color} {i.__class__.__name__} needs water")
                else:
                    print(f"The {i.color} {i.__class__.__name__} doesnt need water")


class Flower():
    absorbing_rate = 0.75
    def __init__(self, color):
        self.color = color
        self.water = 0

class Tree():
    absorbing_rate = 0.4
    def __init__(self, color):
        self.color = color
        self.water = 0

        