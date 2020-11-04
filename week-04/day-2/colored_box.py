from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
def rectangle(x1,y1,x2,y2):
    
    first_line = canvas.create_line(x1, y1, x2, y1, fill='red', width ="2")
    second_line = canvas.create_line(x1, y1, x1, y2, fill='green', width ="2")
    third_line = canvas.create_line(x2, y1, x2, y2, fill='blue', width ="2")
    fourth_line = canvas.create_line(x1, y2, x2, y2, fill='yellow', width ="2")

rectangle(50, 50, 150, 100 )
root.mainloop()