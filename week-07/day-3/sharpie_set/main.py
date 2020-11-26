from sharpie_set import Sharpie_set
from sharpie import Sharpie

green = Sharpie("green", 0.1)
red = Sharpie("red", 0.2)
orange = Sharpie("orange", 0.3)

new_set = Sharpie_set()

green.use()

new_set.add(green)
new_set.add(red)
new_set.add(orange)

print(new_set.count_usable())

