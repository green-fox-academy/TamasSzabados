from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws one square and takes 1 parameters:
# The square size
# and draws a square of that size to the center of the canvas.
# Draw 3 squares with that function.
# Avoid code duplication.

def rectangle(size, color="green"):
    x1 = 150-size/2
    y1 = 150-size/2
    x2 = 150+size/2
    y2 = 150+size/2
    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=color, width ="2")

rectangle(250)
rectangle(150)
rectangle(50)

root.mainloop()





