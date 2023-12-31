import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("./etud.db")
conn.execute("CREATE TABLE IF NOT EXISTS etudiant(cne INTEGER, nom TEXT, prenom TEXT, filliere TEXT)")
conn.commit()
conn.close()

def ajouter():
    cne = e1.get()
    conn = sqlite3.connect("./etud.db")
    conn.execute("INSERT INTO etudiant VALUES (?,?,?,?)", (cne, e2.get(), e3.get(), e4.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Enregistrement réussi")
    update_treeview()

def supprimer():
    selected = tree.selection()
    if selected:
        conn = sqlite3.connect("./etud.db")
        cne = tree.item(selected, "values")[0]
        conn.execute("DELETE FROM etudiant WHERE cne=?", (cne,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Suppression réussie")
        update_treeview()

def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    conn = sqlite3.connect("./etud.db")
    cursor = conn.execute("SELECT * FROM etudiant")

    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

    conn.close()

def update_etudiant():
    selected_item = tree.selection()
    if selected_item:
        cne = e1.get()
        nom = e2.get()
        prenom = e3.get()
        filliere = e4.get()

        conn = sqlite3.connect("./etud.db")
        conn.execute("UPDATE etudiant SET nom=?, prenom=?, filliere=? WHERE cne=?", (nom, prenom, filliere, cne))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Mise à jour réussie")
        update_treeview()

root = tk.Tk()
root.title("Gestion des employés")
root.geometry("1200x700+0+0")

l1 = tk.Label(root, text="CNE:")
l1.place(relx=0.1, rely=0.1)
e1 = tk.Entry(root, width=40)
e1.place(relx=0.2, rely=0.1)

l2 = tk.Label(root, text="Nom :")
l2.place(relx=0.1, rely=0.2)
e2 = tk.Entry(root, width=40)
e2.place(relx=0.2, rely=0.2)

l3 = tk.Label(root, text="Prenom :")
l3.place(relx=0.1, rely=0.3)
e3 = tk.Entry(root, width=40)
e3.place(relx=0.2, rely=0.3)

l4 = tk.Label(root, text="Filliere :")
l4.place(relx=0.1, rely=0.4)
e4 = tk.Entry(root, width=40)
e4.place(relx=0.2, rely=0.4)

columns = ("CNE", "Nom", "Prenom", "Filliere")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.35)

btn_ajouter = tk.Button(root, text="Ajouter", command=ajouter)
btn_ajouter.place(relx=0.35, rely=0.5)

btn_supprimer = tk.Button(root, text="Supprimer", command=supprimer)
btn_supprimer.place(relx=0.6, rely=0.5)

btn_update = tk.Button(root, text="Mettre à jour", command=update_etudiant)
btn_update.place(relx=0.8, rely=0.5)

update_treeview()

root.mainloop()
