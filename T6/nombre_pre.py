from tkinter import *


def Premier():
    contenu = entry.get()
    N = int(contenu)
    for i in range(2, N + 1):
        est_premier = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                est_premier = False
                break
        if est_premier:
            textarea.insert(END, str(i) + "\t")


fen1 = Tk()
fen1.title("Nombres premiers")

label1 = Label(fen1, text="Donner un nombre")
label1.grid(row=1, column=1)
entry = Entry(fen1)
entry.grid(row=1, column=2)

label2 = Label(fen1, text="Les nombres premiers sont")
label2.grid(row=2, column=1)

textarea = Text(fen1, width=30, height=10)
textarea.grid(row=2, column=2)

bouton = Button(fen1, text="résultats", command=Premier)
bouton.grid(row=3, column=1)

fen1.mainloop()