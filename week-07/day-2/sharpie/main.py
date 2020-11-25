from sharpie import Sharpie

red_sharpie = Sharpie("red", 1.3)
red_sharpie.use()
print(red_sharpie.get_ink())

print(red_sharpie.get_color())
red_sharpie.set_color("green")
print(red_sharpie.get_color())