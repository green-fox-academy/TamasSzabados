from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a square drawing function that takes 2 parameters:
# The square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# Create a loop that fills the canvas with rainbow colored squares (red, orange, yellow, green, blue, indigo, violet).


def rectangle(size, color="green"):
    x1 = 150-size/2
    y1 = 150-size/2
    x2 = 150+size/2
    y2 = 150+size/2
    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=color, width ="2")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(len(colors)):
    rectangle(150-(i*20),colors[i])
root.mainloop()