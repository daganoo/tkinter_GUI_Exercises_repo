from tkinter import *
from random import randrange

case_size = 40
def damier():
    can.delete('all')
    for row in range(10):
        for col in range(10):
            x1 = col * case_size
            y1 = row * case_size
            x2 = x1 + case_size
            y2 = y1 + case_size
            couleur = "blue" if (row + col) % 2 == 0 else "white"

            can.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
def pions():
    i = randrange(10)
    j = randrange(10)
    can.create_oval(i*case_size, j*case_size, (i+1)*case_size, (j+1)*case_size, fill="black")



window = Tk()
can = Canvas(window, height=400, width=400)
can.pack()

Button(window, text="Damier", command=damier).pack(side=LEFT)
Button(window, text="pions", command=pions).pack(side=RIGHT)
window.mainloop()