import tkinter as tk
from tkinter import ttk

def toggle_password_visibility():
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

root = tk.Tk()
root.title("Interface Tkinter")

email_label = ttk.Label(root, text="Email:")
email_entry = ttk.Entry(root)

password_label = ttk.Label(root, text="Mot de passe:")
password_entry = ttk.Entry(root, show="*")

show_password = tk.BooleanVar()
show_password.set(False)

show_password_button = ttk.Checkbutton(root, text="Afficher Mot de Passe", variable=show_password, command=toggle_password_visibility)


login_button = ttk.Button(root, text="Se connecter", command=lambda: print(f"Email: {email_entry.get()}, Mot de passe: {password_entry.get()}"))

email_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
email_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

show_password_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")
login_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
