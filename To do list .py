import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def delete_all_tasks():
    if messagebox.askyesno("Delete All", "Are you sure you want to delete all tasks?"):
        task_listbox.delete(0, tk.END)

def close_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x300")
root.configure(bg="lightblue")

# Title
title_label = tk.Label(root, text="TO-DO-LIST", font=("Helvetica", 16, "bold"), bg="lightblue")
title_label.pack(pady=5)

# Task entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=5)

add_btn = tk.Button(button_frame, text="Add", width=10, bg="gold", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

remove_btn = tk.Button(button_frame, text="Remove", width=10, bg="gold", command=remove_task)
remove_btn.grid(row=0, column=1, padx=5)

delete_all_btn = tk.Button(button_frame, text="Delete All", width=10, bg="gold", command=delete_all_tasks)
delete_all_btn.grid(row=0, column=2, padx=5)

# Listbox
task_listbox = tk.Listbox(root, width=50, height=8)
task_listbox.pack(pady=10)

# Exit Button
exit_btn = tk.Button(root, text="Exit / Close", width=50, bg="gold", command=close_app)
exit_btn.pack(pady=5)

root.mainloop()