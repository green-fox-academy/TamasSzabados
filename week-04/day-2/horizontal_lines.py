from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# Draw at least 3 lines with that function using a loop.
def horizontal(x, y):
    x2 = x + 50
    y2 = y
    
    first_line = canvas.create_line(x, y, x2, y2, fill='green', width ="2")
    
for i in range(1,300, 10):  
    horizontal(0, i+50)


root.mainloop()