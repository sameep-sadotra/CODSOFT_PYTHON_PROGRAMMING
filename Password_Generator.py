import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_var.get()
    complexity = complexity_var.get()

    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for password length.")
        return

    length = int(length)

    if complexity == "Simple":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def reset_password():
    password_var.set("")
    username_var.set("")
    length_var.set("")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

length_var = tk.StringVar()
complexity_var = tk.StringVar()
password_var = tk.StringVar()
username_var = tk.StringVar()

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

tk.Label(frame, text="Username:", bg="#f0f0f0").grid(row=0, column=0)
username_entry = tk.Entry(frame, textvariable=username_var, width=20)
username_entry.grid(row=0, column=1)

tk.Label(frame, text="Password Length:", bg="#f0f0f0").grid(row=1, column=0)
length_entry = tk.Entry(frame, textvariable=length_var, width=10)
length_entry.grid(row=1, column=1)

tk.Label(frame, text="Complexity:", bg="#f0f0f0").grid(row=2, column=0)
complexity_options = ["Simple", "Medium", "Strong"]
complexity_menu = tk.OptionMenu(frame, complexity_var, *complexity_options)
complexity_menu.grid(row=2, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#77dd77")
generate_button.pack(pady=10)

password_frame = tk.Frame(root, bg="#f0f0f0")
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="Your Password:", bg="#f0f0f0")
password_label.pack()
password_display = tk.Label(password_frame, textvariable=password_var, bg="#f0f0f0", font=("Courier New", 12, "bold"))
password_display.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#ffa07a")
copy_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_password, bg="#ffcccb")
reset_button.pack(pady=5)

root.mainloop()
