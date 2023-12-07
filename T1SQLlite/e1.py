import tkinter as tk
import sqlite3

def create_table():
    # Create the 'info' table in the SQLite database
    conn = sqlite3.connect("Music.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS info (
            name TEXT,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def submit():
    try:
        # Get values from entry fields
        name_value = name_entry.get()
        age_value = age_entry.get()

        # Insert data into SQLite database
        conn = sqlite3.connect("Music.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO info (name, age) VALUES (?, ?)", (name_value, age_value))
        conn.commit()
        conn.close()

        # Display the inserted data in a text file
        with open("output.txt", "a") as file:
            file.write(f"Name: {name_value}, Age: {age_value}\n")

        # Clear entry fields
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

    except Exception as e:
        print(f"Error: {e}")

# Create the 'info' table
create_table()

# Create the main application window
app = tk.Tk()
app.title("Data Entry and Display")

# Create and place the Name label and entry field
name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the Age label and entry field
age_label = tk.Label(app, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

age_entry = tk.Entry(app)
age_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the Submit button
submit_button = tk.Button(app, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
app.mainloop()
