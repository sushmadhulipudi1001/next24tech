# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x200")
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    messagebox.showinfo("Form Submission", f"Name: {name}\nEmail: {email}\nAge: {age}")

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)
root.mainloop()

