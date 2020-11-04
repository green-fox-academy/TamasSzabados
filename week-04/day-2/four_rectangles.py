from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Draw four different size and color rectangles.
# Avoid code duplication.
def rectangle(x1,y1,x2,y2, color="green"):
    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=color, width ="2")

rectangle(10,10,30,30, "blue")
rectangle( 30, 30, 70, 70, "red")
rectangle( 70, 70,90,90,"yellow")
rectangle( 90, 90,150,150)

root.mainloop()