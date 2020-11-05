from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


def to_center(x1, y1, x2, y2):
    first_line = canvas.create_line(x1, y2, x2, y2, fill='red', width ="2")

x1= 150
y1=150
n1, n2 = 0, 1
count = 0
while count < 30:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    
 

    to_center(x1,y1,x1+nth,y1-nth)
  
    to_center(x1,y1,x1-nth,y1+nth)
    
    count += 1


    

root.mainloop()