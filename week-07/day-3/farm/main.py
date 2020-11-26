from animals import Animal
from farm import Farm

gekko = Animal()
python = Animal()
dog = Animal()
cat = Animal()
frog = Animal()

frog.play()
frog.play()
frog.play()
frog.play()

new_farm = Farm()

new_farm.add(gekko)
new_farm.add(python)
new_farm.add(cat)
new_farm.add(frog)
new_farm.add(dog)
new_farm.breed()

new_farm.slaughter()