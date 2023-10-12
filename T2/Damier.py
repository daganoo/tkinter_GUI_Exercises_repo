import tkinter as tk
from random import randrange

def draw_damier(event=None):
    global square_size
    canvas.delete("all")
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    square_size = min(canvas_width // columns, canvas_height // rows)

    for row in range(rows):
        for col in range(columns):
            color_index = (row + col) % 2
            x0, y0 = col * square_size, row * square_size
            x1, y1 = x0 + square_size, y0 + square_size
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[color_index])

def add_pawn():
    i = randrange(columns)
    j = randrange(rows)
    x0, y0 = i * square_size, j * square_size
    x1, y1 = x0 + square_size, y0 + square_size
    canvas.create_oval(x0, y0, x1, y1, fill="black")

root = tk.Tk()
root.title("Damier")

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

rows, columns, square_size = 10, 10, 40
colors = ["white", "blue"]

draw_button = tk.Button(root, text="Damier", command=draw_damier)
draw_button.pack(side="left")

pawn_button = tk.Button(root, text="Dame", command=add_pawn)
pawn_button.pack(side="left")

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(side="right")

# Bind canvas to resize event
canvas.bind("<Configure>", draw_damier)

root.mainloop()
