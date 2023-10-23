from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

def lines():
    colors = ['red', 'green', 'blue']
    color_index = 0  
    for i in range(0, 500, 6):
        color = colors[color_index]
        canvas.create_line(0, i, 500, i, fill=color)
        color_index = (color_index + 1) if color_index < 2 else 0

b1 = Button(root, text="draw", command=lines)
b1.pack()
root.mainloop()
