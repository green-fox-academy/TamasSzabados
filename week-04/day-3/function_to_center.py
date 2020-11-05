from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws a single line and takes 2 parameters:
# The x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# Fill the canvas with lines from the edges, every 20 px, to the center.
def to_center(x, y):
    x2 = 150
    y2 = 150
    
    first_line = canvas.create_line(x, y, x2, y2, fill='green', width ="1")

for i in range(0,300, 20):
    to_center(0, i)
    to_center(300,i)
    to_center(i,0)
    to_center(i,300)

root.mainloop()