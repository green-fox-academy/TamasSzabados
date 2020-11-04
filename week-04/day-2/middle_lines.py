from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

red_line = canvas.create_line(0, 150, 300, 150, fill='red', width ="2")
green_line = canvas.create_line(150, 0, 150, 300, fill='green', width ="2")
# draw a red horizontal line to the canvas' middle.
# draw a green vertical line to the canvas' middle.

root.mainloop()

