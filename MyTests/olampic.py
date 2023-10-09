from tkinter import *

fenetre = Tk()
fenetre.title("Anneaux olympiques")

# Fonction pour dessiner un anneau olympique
def dessiner_anneau(couleur, x, y):
    canvas.create_oval(x, y, x + 100, y + 100, outline=couleur, width=5)

# Fonctions pour dessiner chaque anneau olympique
def dessiner_bleu():
    dessiner_anneau('blue', 50, 50)

def dessiner_jaune():
    dessiner_anneau('yellow', 170, 50)

def dessiner_noir():
    dessiner_anneau('black', 270, 50)

def dessiner_vert():
    dessiner_anneau('green', 105, 100)

def dessiner_rouge():
    dessiner_anneau('red', 215, 100)

# Fonction pour fermer la fenêtre
def quitter():
    fenetre.quit()

canvas = Canvas(fenetre, width=500, height=300, bg='white')
canvas.pack()

# Créer les 5 boutons pour dessiner les anneaux
bouton_bleu = Button(fenetre, text="Bleu", command=dessiner_bleu)
bouton_bleu.pack()

bouton_jaune = Button(fenetre, text="Jaune", command=dessiner_jaune)
bouton_jaune.pack()

bouton_noir = Button(fenetre, text="Noir", command=dessiner_noir)
bouton_noir.pack()

bouton_vert = Button(fenetre, text="Vert", command=dessiner_vert)
bouton_vert.pack()

bouton_rouge = Button(fenetre, text="Rouge", command=dessiner_rouge)
bouton_rouge.pack()

# Bouton pour quitter
bouton_quitter = Button(fenetre, text="Quitter", command=quitter)
bouton_quitter.pack()

fenetre.mainloop()
