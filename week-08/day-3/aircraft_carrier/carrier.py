from aircraft import Aircraft, F16, F35


class Carrier():
    def __init__(self, ammo, health):
        self.ammo = ammo
        self.health = health
        self.aircraft = []
        self.total_damage = 0

    def add(self, aircraft):
        self.aircraft.append(aircraft)

    def fill(self):
        ammo_needed = 0
        for i in self.aircraft:
            ammo_needed += (i.max_ammo-i.ammo)
        try:
            if self.ammo < ammo_needed:
                for i in self.aircraft:
                    if i.isPriority:
                        remaining = i.refill(self.ammo)
                        self.ammo += remaining
                for i in self.aircraft:
                        remaining = i.refill(self.ammo)
                        self.ammo += remaining
        except:
            print("Run out of ammo")

    def fight(self,carrier):
        for i in self.aircraft:
            carrier.health -= i.fight()

    def get_status(self):
        if self.health <=0:
            return "It's dead Jim :("
        else:
            return f"THP: {self.health}, Aircraft count: {len(self.aircraft)}, Ammo Storage: {self.ammo}, Total damage: {self.total_damage}"
            for i in self.aircraft:
                return f"Type {i.__class__.__name__}, Ammo: {i.ammo}, Base Damage: {i.baseDamage}, All Damage: {i.damage_dealt}"


