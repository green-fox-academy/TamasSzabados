from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Fill the canvas with a checkerboard pattern.
SIZE=10
def rectangle(x1,y1,color):
    
    x2 = x1 + SIZE
    y2 = y1 + SIZE
    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=color, width ="1")

color= 'white'
for i in range(0,100,1):
    for k in range(0,100,1):
        rectangle(i*SIZE, k*SIZE, color)
        if color == 'white':
            color = 'black'
        else:    
            color = 'white'

    if color == 'white':
        color = 'black'
    else:    
        color = 'white'

root.mainloop()