from tkinter import *

window = Tk()
window.title("Bigger Point in tkinter")

canvas = Canvas(window, width=700, height=500)
canvas.pack()

canvas.create_polygon((0,0, 100, 150, 300, 300), fill="red")

window.mainloop()
