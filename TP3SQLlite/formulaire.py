import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

def quitter():
    fenetre.destroy()


def enregistrer_utilisateur():
    prenom = entry_prenom.get()
    nom = entry_nom.get()
    pays = combo_pays.get()
    langage = var_langage.get()
    genre = var_genre.get()

   
    connexion = sqlite3.connect('utilisateurs.db')
    curseur = connexion.cursor()

    if not prenom or not nom or not pays or not langage or not genre:
        messagebox.showerror("Champs vides", "Veuillez remplir tous les champs du formulaire.")
        return

    curseur.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prenom TEXT,
            nom TEXT,
            pays TEXT,
            langage TEXT,
            genre TEXT
        )
    ''')

    curseur.execute('''
        INSERT INTO utilisateurs (prenom, nom, pays, langage, genre)
        VALUES (?, ?, ?, ?, ?)
    ''', (prenom, nom, pays, langage, genre))

    connexion.commit()

    connexion.close()

    with open("form.txt", "a") as file:
        file.write(f"Name: {prenom}, Age: {nom}, pays: {pays}, langage: {langage}, genre: {genre}\n")

    messagebox.showinfo("Enregistrement réussi", "L'utilisateur a été enregistré avec succès.")


fenetre = tk.Tk()
fenetre.title("Formulaire d'enregistrement")

label_prenom = tk.Label(fenetre, text="Prénom:")
label_prenom.grid(row=0, column=0, padx=10, pady=10)
entry_prenom = tk.Entry(fenetre)
entry_prenom.grid(row=0, column=1, padx=10, pady=10)

label_nom = tk.Label(fenetre, text="Nom:")
label_nom.grid(row=1, column=0, padx=10, pady=10)
entry_nom = tk.Entry(fenetre)
entry_nom.grid(row=1, column=1, padx=10, pady=10)

label_pays = tk.Label(fenetre, text="Pays:")
label_pays.grid(row=2, column=0, padx=10, pady=10)
liste_pays = ["France", "Canada", "États-Unis", "Autre"]
combo_pays = ttk.Combobox(fenetre, values=liste_pays)
combo_pays.grid(row=2, column=1, padx=10, pady=10)

label_langage = tk.Label(fenetre, text="Prog Language:")
label_langage.grid(row=3, column=0, padx=10, pady=10)
var_langage = tk.StringVar()
check_java = tk.Checkbutton(fenetre, text="Java", variable=var_langage, onvalue="Java")
check_java.grid(row=3, column=1, padx=10, pady=5, sticky="w")
check_python = tk.Checkbutton(fenetre, text="Python", variable=var_langage, onvalue="Python")
check_python.grid(row=3, column=2, padx=10, pady=5, sticky="w", ipady=5)
check_cpp = tk.Checkbutton(fenetre, text="C++", variable=var_langage, onvalue="C++")
check_cpp.grid(row=3, column=3, padx=10, pady=5, sticky="w", ipady=5)

label_genre = tk.Label(fenetre, text="Genre:")
label_genre.grid(row=4, column=0, padx=10, pady=10)
var_genre = tk.StringVar()
radio_feminin = tk.Radiobutton(fenetre, text="Féminin", variable=var_genre, value="Féminin")
radio_feminin.grid(row=4, column=1, padx=10, pady=5, sticky="w")
radio_masculin = tk.Radiobutton(fenetre, text="Masculin", variable=var_genre, value="Masculin")
radio_masculin.grid(row=4, column=2, padx=10, pady=5, sticky="w", ipady=5)

bouton_submit = tk.Button(fenetre, text="Soumettre", command=enregistrer_utilisateur)
bouton_submit.grid(row=5, column=0, columnspan=2, pady=10)
bouton1_quitter = tk.Button(fenetre, text="Quitter", command=quitter)
bouton1_quitter.grid(row=6, column=0, columnspan=2, pady=10)

# Lancement de la boucle principale
fenetre.mainloop()
