from tkinter import *

window = Tk()
window.title("Bigger Point in tkinter")

canvas = Canvas(window, width=700, height=500)
canvas.pack()
canvas.create_oval((50,50,200,200))
canvas.create_oval((200,50,350,200))
canvas.create_oval((350,50,500,200))
canvas.create_oval((125,125,275,275))
canvas.create_oval((275,125,425,275))

b1 = Button(window, text="drow the circle")
b1.pack()
window.mainloop()
