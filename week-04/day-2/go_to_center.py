from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# Draw at least 3 lines with that function using a loop.
def to_center(x, y):
    x2 = 150
    y2 = 150
    
    first_line = canvas.create_line(x, y, x2, y2, fill='red', width ="2")
    
for i in range(1,300, 10):  
    to_center(i, i+50)

root.mainloop()