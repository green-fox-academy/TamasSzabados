class Sharpie():
    def __init__(self, color = "" , width= float()):
        self.color = color
        self.width = width
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 1
        return self.ink_amount

    def get_ink(self): 
        return self.ink_amount

    def get_width(self):
        return self.width

    def get_color(self):
        return self.color

    def set_width(self, width):
        if type(width) != float:
            raise TypeError("width must be a float")
        else:
            self.width = width
        return self.width

    def set_color(self, color):
        if type(width) != float:
            raise TypeError("color must be a string")
        else:
            self.color = color
        return self.color
