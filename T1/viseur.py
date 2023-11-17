from tkinter import *
from random import randrange

def drawline():
    global x1, y1, x2, y2, cou1
    can1.create_line(x1, y1, x2, y2, width=1, fill=cou1)
    y2, y1 = y2 + 10, y1 - 10

def changecolor():
    global cou1
    pal = ['blue', 'black', 'green','red']
    c = randrange(4)
    cou1 = pal[c]

x1, y1, x2, y2 = 10, 190, 190, 10
cou1 = 'dark green'

def drawline_2():
    can1.create_line(100, 0, 100, 200, fill='red', width=1)
    can1.create_line(0,100, 200, 100, fill='red', width=1)

window = Tk()
can1 = Canvas(window, bg='grey', height=200, width=200)
can1.pack(side=LEFT)
bou1 = Button(window, text='Quitter', command=window.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(window, text='Tracer ligne', command=drawline)
bou2.pack()
bou3 = Button(window, text='Autre couleur', command=changecolor)
bou3.pack()
bou4 = Button(window, text='Viseur +', command=drawline_2)
bou4.pack()
window.mainloop()