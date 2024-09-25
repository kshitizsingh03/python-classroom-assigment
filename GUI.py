import tkinter as tk
from formate import organize_files

root = tk.Tk()
root.title("My Input Window")

label = tk.Label(root, 
                 text="Enter Directory Path",
                 font=("Helvetica", 16),
                 fg="red",
                 bg="White",
                 padx=100,
                 pady=100)

label.pack()

entry = tk.Entry(root,
                 font=("Arial", 14),
                 fg="black",
                 bg="lightgrey")

entry.pack(pady=10)

def on_button_click():
    organize_files(entry.get())

button = tk.Button(root, 
                   text="Submit",
                   font=("Arial", 14),
                   fg="white",
                   bg="red", 
                   activebackground="lightgreen",
                   command=on_button_click)


button.pack(pady=20)

root.mainloop()