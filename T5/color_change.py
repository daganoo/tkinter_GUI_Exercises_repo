import tkinter as tk

def move_square(event):
    key = event.keysym

    if key == "Up":
        canvas.move(square, 0, -10)
    elif key == "Down":
        canvas.move(square, 0, 10)
    elif key == "Left":
        canvas.move(square, -10, 0)
    elif key == "Right":
        canvas.move(square, 10, 0)

root = tk.Tk()
root.title("Move Square with Arrow Keys")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

square = canvas.create_rectangle(190, 190, 210, 210, fill="black")

root.bind("<Up>", move_square)
root.bind("<Down>", move_square)
root.bind("<Left>", move_square)
root.bind("<Right>", move_square)

root.mainloop()