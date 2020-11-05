from tkinter import *
import math

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Reproduce this:
# [https://github.com/green-fox-academy/teaching-materials/blob/master/workshop/drawing/assets/r4.png]

def rectangle(x1, size, color="purple"):
    y1=x1
    x2 = x1 + size
    y2 = y1 + size
    rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=color, width ="1")

count = 1
for i in range(1,30):
    rectangle(count*10, i*10)
    count+=i
    

root.mainloop()