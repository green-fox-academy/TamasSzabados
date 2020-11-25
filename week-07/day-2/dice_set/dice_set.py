import random

class DiceSet(object):

    def __init__(self):
        self.dices = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dices)):
            self.dices[i] = random.randint(1, 6)
        return self.dices

    def get_current(self, index = None):
        if index != None:
            return self.dices[index]
        else:
            return self.dices

    def reroll(self, index = None):
        if index != None:
            self.dices[index] = random.randint(1, 6)
        else:
            self.roll()


dice_set = DiceSet()
print(dice_set.get_current())
dice_set.roll()
print(dice_set.get_current())
dice_set.reroll(3)
print(dice_set.get_current(3))
print(dice_set.get_current())

count=0
while dice_set.get_current() != [6,6,6,6,6,6]:
    dice_set.reroll()
    count +=1

print(count)
print(dice_set.get_current())


count2=0
for i in dice_set.dices:
    if i != 6:
        dice_set.reroll(i.index())
        count2 +=1

print(count2)
print(dice_set.get_current())
# - You have a `DiceSet` class which has 6 dices
# - You can roll all of them with `roll()`
# - Check the current rolled numbers with `get_current()`
# - You can reroll with `reroll()`
# - Your task is to roll the dices until all of the dices are 6