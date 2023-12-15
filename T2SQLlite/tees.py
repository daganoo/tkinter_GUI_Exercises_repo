from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import sqlite3


def browse_file(entry):
    filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("Text files", ".txt"), ("all files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def add_client():
    name = entryName.get()
    phone = entryPhone.get()
    photo = entryPhoto.get()
    more_info = entryMore.get()

    cursor.execute("INSERT INTO clients (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()

    tree.insert("", tk.END, values=(cursor.lastrowid, name, phone))

def delete_selection():
    selected_item = tree.selection()
    client_id = tree.item(selected_item, "values")[0]

    cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
    conn.commit()

    tree.delete(selected_item)

def edit_selection():
    selected_item = tree.selection()
    client_id = tree.item(selected_item, "values")[0]
    name = entryName.get()
    phone = entryPhone.get()

    cursor.execute("UPDATE clients SET name=?, phone=? WHERE id=?", (name, phone, client_id))
    conn.commit()

    tree.item(selected_item, values=(client_id, name, phone))

def sort_by_name():
    items = tree.get_children()
    items = sorted(items, key=lambda x: tree.item(x, "values")[1])
    tree.delete(*tree.get_children())
    for item in items:
        tree.insert("", tk.END, values=tree.item(item, "values"))

def exit_page():
    root.destroy()

conn = sqlite3.connect("Carnet d'Adresses.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS clients 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT)''')
conn.commit()

root = Tk()
root.title("Carnet d'Adresses")
root.geometry("550x480")

lblTitle = Label(root, text="Carnet d'Adresses", font=("Arial", 21), bg="green", fg="white")
lblTitle.place(x=0, y=0, width=250)

lbSearchByName = Label(root, text="Chercher par nom :", bg="green", fg="white")
lbSearchByName.place(x=250, y=0, width=120)
entrySearchByName = Entry(root)
entrySearchByName.place(x=380, y=0, width=160)

lbSearchByPhone = Label(root, text="Chercher par num :", bg="green", fg="white")
lbSearchByPhone.place(x=250, y=17, width=120)
entrySearchByPhone = Entry(root)
entrySearchByPhone.place(x=380, y=20, width=160)

lblName = Label(root, text="Nom & prénom :", bg="blue", fg="white")
lblName.place(x=5, y=50, width=125)
entryName = Entry(root)
entryName.place(x=140, y=50, width=400)

lblPhone = Label(root, text="Num de Telephone :", bg="blue", fg="white")
lblPhone.place(x=5, y=80, width=125)
entryPhone = Entry(root)
entryPhone.place(x=140, y=80, width=400)

lblPhoto = Label(root, text="Photo :", bg="blue", fg="white")
lblPhoto.place(x=5, y=110, width=125)
bPhoto = Button(root, text="Upload", bg="green", fg="white", command=lambda: browse_file(entryPhoto))
bPhoto.place(x=480, y=110, height=25)
entryPhoto = Entry(root)
entryPhoto.place(x=140, y=110, width=320)

lblMore = Label(root, text="Plus d'info :", bg="blue", fg="white")
lblMore.place(x=5, y=140, width=125)
entryMore = Entry(root)
entryMore.place(x=140, y=140, width=400)

bAdd = Button(root, text="Ajouter client", bg="green", fg="white", command=add_client)
bAdd.place(x=5, y=170, width=255)

bDelete = Button(root, text="Supp la Selection", bg="green", fg="white", command=delete_selection)
bDelete.place(x=5, y=205, width=255)

bEdit = Button(root, text="Modifier la Selection", bg="green", fg="white", command=edit_selection)
bEdit.place(x=5, y=240, width=255)

bSort = Button(root, text="Trier par nom", bg="green", fg="white", command=sort_by_name)
bSort.place(x=5, y=275, width=255)

bExit = Button(root, text="Quitter la page", bg="green", fg="white", command=exit_page)
bExit.place(x=5, y=310, width=255)

tree = ttk.Treeview(root, columns=(1, 2, 3), height=5, show="headings")
tree.place(x=265, y=170, width=290, height=175)

tree.heading(1, text="ID")
tree.heading(2, text="NOM")
tree.heading(3, text="TELEPHONE")

tree.column(1, width=50)
tree.column(2, width=100)
tree.column(3, width=100)

root.mainloop()

conn.close()