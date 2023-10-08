from tkinter import *
from random import randrange

fen1 = Tk()

# définition des fonctions

def drawline():
    "tracé d'une ligne dans le canvas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
    # modification des cordonees pour la line suivante
    y2, y1 = y2+20, y1-20


def changecolor():
    "changement de color aléatoire"
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green',
           'red', 'blue', 'orange', 'yellow']
    c = randrange(8)  # pou génère un nombe aléatoire de 0 à 7
    coul = pal[c]

# -------------  programme principal  -------------

# les variable suivante seront utilisé de manière globale
x1, y1, x2, y2 = 10, 190, 190, 10  # coordonnées de la ligne
coul = 'dark green'  # color de la ligne

can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text="tracer une ligne", command=drawline)
bou2.pack()
bou3 = Button(fen1, text="Autre couleur", command=changecolor)
bou3.pack()


fen1.mainloop()
fen1.destroy()
