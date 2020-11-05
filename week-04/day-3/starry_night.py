from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = "black")
canvas.pack()

# Draw the night sky:
#  - The background should be black
#  - The stars should be small squares
#  - The stars should have random positions on the canvas
#  - The stars should have random color (some shade of grey)


def rectangle(x1,y1, size, color="white"):
    x2 = x1 + size
    y2 = y1 + size

    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=color, width ="1")


for i in range(150):
    rectangle(random.randint(i,300),random.randint(i,300), random.randint(1, 3))



root.mainloop()