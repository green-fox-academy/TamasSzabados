class Aircrafts():
    def __init__(self):
        self.ammo = 0
        self.max_ammo = 0
        self.base_damage = 0
        

    def fight(self):
        damage = self.ammo * self.base_damage
        self.ammo = 0
        return damage

    def refill(self, number):
        fuel_needed = self.max_ammo-self.ammo
        if number >= fuel_needed:
            self.ammo = self.max_ammo
            return number - fuel_needed
        else:
            self.ammo += number
            return 0
        
    def get_type(self):
        print(f"{self.__class__.__name__}")

    def get_status(self):
        print(f" Type: {self.__class__.__name__} , Ammo: {self.ammo} , Base Damage: {self.base_damage}, All Damage: {self.all_damage}")
    

    def is_priority(self):
        if str(self.__class__.__name__) = "F16":
            return False
        if str(self.__class__.__name__) = "F35":
            return True

class F16(Aircrafts):
    def __init__(self):
        super().__init__()
        self.max_ammo = 8
        self.base_damage = 30

class F35(Aircrafts):
    def __init__(self):
        super().__init__()
        self.max_ammo = 12
        self.base_damage = 50

class Carrier():
    def __init__(self, ammo, health):
        self.aircrafts = []
        self.ammo = ammo
        self.health = health
        self.damage = 0

    def add(self, aircraft):
        self.aircrafts.append(aircraft)
        return self.aircrafts

    def fill(self):
        try:
            for aircraft in self.aircrafts:
                if self.ammo > (aircraft.max_ammo - aircrart.ammo) and aircraft.is_priority():
                    self.ammo -= aircraft.refill(self.ammo)
            for aircraft in self.aircrafts:
                if self.ammo > (aircraft.max_ammo - aircrart.ammo):
                    self.ammo -= aircraft.refill(self.ammo)
        except:
            print("Run out of ammo")

    def fight(self, carrier):
        for aircraft in carrier.aircrafts:
            self.damage += aircraft.fight()

    @property
    def get_damage(self):
        return self.damage


    def get_status(self):
        print(f" HP: {self.health} , Aircraft count: {len(self.aircrafts)}, Ammo Storage: {self.ammo}, Total damage: {self.get_damage}")
        for aircraft in aircrafts:
            print(f" Type: {self.__class__.__name__} , Ammo: {self.ammo} , Base Damage: {self.base_damage}, All Damage: {self.all_damage}")
        if self.health <=0:
            return "It's dead Jim :("





