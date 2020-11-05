from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that takes 1 parameter:
# A list of [x, y] points
# and connects them with green lines.
# Connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# Connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

box = [[10, 10], [290,  10], [290, 290], [10, 290]]
list1 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]


def connect_dots(args):
    for i in range(0,len(args)-1):
        x1 = args[i][0]
        y1 = args[i][1]
        x2 = args[i+1][0]
        y2 = args[i+1][1]
        line = canvas.create_line(x1, y1, x2, y2, fill='green', width ="1")
        
        print(x1, y1, x2, y2)
    
connect_dots(box)



root.mainloop()