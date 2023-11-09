from tkinter import *

def update_oval_coordinates(dx, dy):
    current_coords = canvas.coords(oval)
    new_x1 = current_coords[0] + dx
    new_y1 = current_coords[1] + dy
    new_x2 = current_coords[2] + dx
    new_y2 = current_coords[3] + dy

    # Ensure the oval stays within the canvas boundaries
    if new_x1 < 0:
        dx = 0
    if new_y1 < 0:
        dy = 0
    if new_x2 > canvas.winfo_width():
        dx = 0
    if new_y2 > canvas.winfo_height():
        dy = 0

    canvas.move(oval, dx, dy)

def move_up():
    update_oval_coordinates(0, -10)

def move_down():
    update_oval_coordinates(0, 10)

def move_left():
    update_oval_coordinates(-10, 0)

def move_right():
    update_oval_coordinates(10, 0)

root = Tk()
canvas = Canvas(root, height=400, width=300, bg="dark gray")
canvas.pack(side=LEFT)

oval = canvas.create_oval(45, 80, 75, 110, fill="red", outline="red")

btn_1 = Button(root, text="Up", command=move_up)
btn_1.pack()
btn_2 = Button(root, text="Down", command=move_down)
btn_2.pack()
btn_3 = Button(root, text="Left", command=move_left)
btn_3.pack()
btn_4 = Button(root, text="Right", command=move_right)
btn_4.pack()

root.mainloop()
