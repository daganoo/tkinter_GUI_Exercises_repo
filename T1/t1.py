from tkinter import *
from random import randrange

fen1 = Tk()

# définition des fonctions

def drawline():
    "tracé d'une ligne dans le canvas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
    # modification des cordonees pour la line suivante
    y2, y1 = y2+10, y1-10

def drawline2():
    x1_v, y1_v, x2_v, y2_v = 250, 10, 250, 500
    x1_h, y1_h, x2_h, y2_h = 10, 250, 500, 250
    can1.create_line(x1_v, y1_v, x2_v, y2_v, width=2, fill='red')
    can1.create_line(x1_h, y1_h, x2_h, y2_h, width=2, fill='red')

def changecolor():
    "changement de color aléatoire"
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green',
           'red', 'blue', 'orange', 'yellow']
    c = randrange(8)  # pou génère un nombe aléatoire de 0 à 7
    coul = pal[c]

# -------------  programme principal  -------------

# les variable suivante seront utilisé de manière globale
x1, y1, x2, y2 = 15, 500, 500, 15  # coordonnées de la ligne
coul = 'dark green'  # color de la ligne

can1 = Canvas(fen1, bg='dark grey', height=650, width=500)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text="tracer une ligne", command=drawline)
bou2.pack()
bou3 = Button(fen1, text="Autre couleur", command=changecolor)
bou3.pack()

bou5 = Button(fen1, text="tracer X", command=drawline2)
bou5.pack()

fen1.mainloop()
fen1.destroy()
