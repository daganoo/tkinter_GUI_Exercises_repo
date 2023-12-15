import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("\n Carnet d'adress")
 
# Top Label
top_label = tk.Label(root, text="Carnet d'adress", font=("Helvetica", 16),bg="blue")
top_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entries for searching by name
search_name_label = tk.Label(root, text="Chercher par nom:")
search_name_label.grid(row=0, column=1, sticky=tk.E, padx=10)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=2, padx=10)

# Labels and Entries for searching by number
search_number_label = tk.Label(root, text="Chercher par Num:")
search_number_label.grid(row=1, column=1, sticky=tk.E, padx=10)

number_entry = tk.Entry(root)
number_entry.grid(row=1, column=2, padx=10)

# Empty row for spacing
tk.Label(root, text="").grid(row=2)

# Labels and Entries for additional information
label1 = tk.Label(root, text="nom et prenom",width=44,bg="green")
label1.grid(row=3, column=0, sticky=tk.E, padx=10)
entry1 = tk.Entry(root, width=68)
entry1.grid(row=3, column=1, padx=10)

label2 = tk.Label(root, text="Num telephone",width=44,bg="green")
label2.grid(row=4, column=0, sticky=tk.E, padx=10,pady=4)
entry2 = tk.Entry(root, width=68)
entry2.grid(row=4, column=1, padx=10)

label3 = tk.Label(root, text="Photo",width=44,bg="green")
label3.grid(row=5, column=0, sticky=tk.E, padx=10)
entry3 = tk.Entry(root, width=68)
entry3.grid(row=5, column=1, padx=10)

button_uplode = tk.Button(root, text="Uplode")
button_uplode.grid(row=5, column=2, padx=10)

label4 = tk.Label(root, text="plus d'info",width=44,bg="green")
label4.grid(row=6, column=0, sticky=tk.E, padx=10,pady=2)
entry4 = tk.Entry(root, width=68)
entry4.grid(row=6, column=1, padx=10)

# Buttons below label4 and entry4
button1 = tk.Button(root, text="Ajoute client", width=44,bg="blue")
button1.grid(row=7, column=0, padx=10)

button2 = tk.Button(root, text="Supprimer la selection", width=44,bg="blue")
button2.grid(row=8, column=0, padx=10)

button3 = tk.Button(root, text="Modifier la selection", width=44,bg="blue")
button3.grid(row=9, column=0, padx=10)

button4 = tk.Button(root, text="Trier par no", width=44,bg="blue")
button4.grid(row=10, column=0, padx=10 )

# Treeview to the right
tree = ttk.Treeview(root)
tree.grid(row=7, column=1, rowspan=4, columnspan=2, padx=10, pady=10)

# Adding columns to the Treeview
tree["columns"] = ("Column 1", "Column 2")
# Defining column headings
tree.heading("#0", text="ID")
tree.heading("Column 1", text="Name")
tree.heading("Column 2", text="Phone")
# Adding sample data to the Treeview

# Run the Tkinter event loop
root.mainloop()
