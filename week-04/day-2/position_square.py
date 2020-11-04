from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws one square and takes 2 parameters:
# The x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# Draw 3 squares with that function.
# Avoid code duplication.

def rectangle(x1,y1, color="green"):
    x2 = x1 +50
    y2 = y1 +50
    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=color, width ="2")

rectangle(10,20)
rectangle(70,20)
rectangle(130,20)
root.mainloop()







