# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
print("Welcome to my cuboid calculator!")
print("Please enter the length:")
l = float(input())
print("Please enter the second width:")
w = float(input())
print("Please enter the first height:")
h = float(input())

area = 2*l*w+2*l*h+2*h*w
volume = l * w * h

print("Surface Area: " + str(area) + "\n" + "Volume: "+ str(volume))
