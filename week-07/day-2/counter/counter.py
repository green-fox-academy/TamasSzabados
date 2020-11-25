class Counter():
    def __init__(self, integer = 0):
        self.integer = integer
        

    def add(self, *args):
        if len(args) ==0:
            self.integer += 1
        if len (args) ==1:
            self.integer += args[0]
        return self.integer

    def get(self):
        return self.integer
        
    def reset(self):
        self.integer = 0
        return self.integer