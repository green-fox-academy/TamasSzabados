class Aircraft():
    def __init__(self):
        self.ammo = 0
        self.max_ammo = 8
        self.base_damage = 30
        self.damage_dealt = 0


    def fight(self):
        self.damage_dealt = self.base_damage * self.ammo
        self.ammo = 0
        return self.damage_dealt


    def refill(self, num):
        remaining_ammo = 0
        required_ammo = self.max_ammo - self.ammo
        if num <= remaining_ammo:
            self.ammo +=num
        else:
            remaining_ammo = num - required_ammo
            self.ammo = self.max_ammo
        return remaining_ammo
            
    def get_type(self):
        print(f"{self.__class__.__name__}")

    def get_status(self):
        return f"Type {self.__class__.__name__}, Ammo: {self.ammo}, Base Damage: {self.base_damage}, All Damage: {self.damage_dealt}" 
        

    def is_priority(self):
        if isinstance(self, F16):
            return False
        elif isinstance(self, F35):
            return True



class F16(Aircraft):
    def __init__(self):
        super().__init__()
        self.max_ammo = 8
        self.base_damage = 30


class F35(Aircraft):
    def __init__(self):
        super().__init__()
        self.max_ammo = 12
        self.base_damage = 50




    

