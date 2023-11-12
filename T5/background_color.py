import tkinter as tk
def on_enter(event):
    canvas.config(bg="red")
def on_leave(event):
    canvas.config(bg="yellow")
root = tk.Tk()
canvas = tk.Canvas(root, width=420, height=300, bg="white")
canvas.pack()
canvas.bind("<Enter>", on_enter)
canvas.bind("<Leave>", on_leave)
root.mainloop()