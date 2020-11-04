from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Reproduce this:
# [https://github.com/green-fox-academy/teaching-materials/blob/master/workshop/drawing/assets/r3.png]
def rectangle(x1, color="purple"):
    y1=x1
    x2 = x1 +10
    y2 = y1 +10
    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=color, width ="1")

for i in range(1,200,10):
    rectangle(i)

root.mainloop()