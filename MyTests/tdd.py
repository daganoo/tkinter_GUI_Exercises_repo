import tkinter as tk

def on_hover(event):
    button.config(bg='lightblue')

def on_leave(event):
    button.config(bg='white')

def on_click(event):
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Hover and Click Events")

# Create a button
button = tk.Button(root, text="Hover me!", bg='white', padx=10, pady=5)
button.pack(pady=20)

# Create a label to display click event
label = tk.Label(root, text="")
label.pack()

# Bind events to the button
button.bind("<Enter>", on_hover)
button.bind("<Leave>", on_leave)
button.bind("<Button>", on_click)

# Start the Tkinter event loop
root.mainloop()
