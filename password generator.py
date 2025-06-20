import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(password_length_entry.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid positive number for password length.")

def accept_password():
    user = username_entry.get()
    pwd = password_entry.get()
    if user and pwd:
        messagebox.showinfo("Accepted", f"Username: {user}\nPassword: {pwd}")
    else:
        messagebox.showwarning("Incomplete", "Please generate a password first.")

def reset_fields():
    username_entry.delete(0, tk.END)
    password_length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="orange")

title = tk.Label(root, text=":PASSWORD GENERATOR:", font=("Arial", 16, "bold"), bg="orange", fg="navy")
title.pack(pady=10)

# Username
tk.Label(root, text="Enter User Name:", bg="orange", font=("Arial", 12, "bold")).pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack()

# Password Length
tk.Label(root, text="Enter Password Length:", bg="orange", font=("Arial", 12, "bold")).pack()
password_length_entry = tk.Entry(root, width=30)
password_length_entry.pack()

# Generated Password
tk.Label(root, text="Generated Password:", bg="orange", font=("Arial", 12, "bold")).pack()
password_entry = tk.Entry(root, width=30)
password_entry.pack()

# Buttons
generate_btn = tk.Button(root, text="GENERATE PASSWORD", bg="khaki", command=generate_password)
generate_btn.pack(pady=5)

accept_btn = tk.Button(root, text="ACCEPT", bg="lightgreen", command=accept_password)
accept_btn.pack(pady=2)

reset_btn = tk.Button(root, text="RESET", bg="white", command=reset_fields)
reset_btn.pack(pady=2)

root.mainloop()