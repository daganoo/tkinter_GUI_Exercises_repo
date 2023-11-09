from tkinter import *

root = Tk()
root.title("Canvas")
canva = Canvas(root, width=500, height=500, bg="white")
canva.pack()
canva.create_line(60, 0, 60, 500, width=195, fill="darkgrey")
canva.create_line(450, 0, 450, 500, width=195, fill="darkgrey")

canva.create_oval(100, 100, 120, 120, fill="red")
canva.create_oval(400, 400, 420, 420, fill="red")
canva.create_oval(100, 400, 120, 420, fill="green")
canva.create_oval(400, 100, 420, 120, fill="green")

def create_rectangle(x, y):
    canva.create_line(x,150,y,350, width=20,fill="yellow")

x, y = 180, 180
for i in range(5):
    canva.create_line(x,150,y,350, width=20,fill="yellow")
    x += 40
    y += 40

def chenge_colore():
    canva.create_oval(100, 100, 120, 120, fill="green")
    canva.create_oval(400, 400, 420, 420, fill="green")
    canva.create_oval(100, 400, 120, 420, fill="red")
    canva.create_oval(400, 100, 420, 120, fill="red")

b1 = Button(root, text="Feu Rouge",command=chenge_colore)
b1.pack()
root.mainloop()
