import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------- Password Generation Logic ---------------- #
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for password length.")
        return

    characters = ''
    if var_letters.get():
        characters += string.ascii_letters
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("No Character Type Selected", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)
    check_strength(password)

def copy_to_clipboard():
    password = result_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# ---------------- Strength Checker ---------------- #
def check_strength(password):
    strength = "Weak"
    if (len(password) >= 8 and
        any(c in string.ascii_lowercase for c in password) and
        any(c in string.ascii_uppercase for c in password) and
        any(c in string.digits for c in password) and
        any(c in string.punctuation for c in password)):
        strength = "Strong"
    elif len(password) >= 6:
        strength = "Medium"
    strength_var.set(f"Password Strength: {strength}")

# ---------------- GUI Setup ---------------- #
root = tk.Tk()
root.title("🔐 Advanced Password Generator")
root.geometry("430x370")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

# --- Heading --- #
tk.Label(root, text="Advanced Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f4f7").pack(pady=10)

# --- Input for Length --- #
length_frame = tk.Frame(root, bg="#f0f4f7")
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#f0f4f7").pack(side='left')
length_entry = tk.Entry(length_frame, font=("Arial", 12), justify='center', width=6)
length_entry.insert(0, "12")
length_entry.pack(side='left', padx=10)

# --- Checkboxes --- #
checkbox_frame = tk.LabelFrame(root, text="Include Characters", font=("Arial", 11, "bold"), padx=10, pady=5, bg="#f0f4f7")
checkbox_frame.pack(pady=10, padx=20, fill='x')

var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(checkbox_frame, text="Letters (A-Z, a-z)", variable=var_letters, bg="#f0f4f7").pack(anchor='w')
tk.Checkbutton(checkbox_frame, text="Numbers (0-9)", variable=var_numbers, bg="#f0f4f7").pack(anchor='w')
tk.Checkbutton(checkbox_frame, text="Symbols (!@#$...)", variable=var_symbols, bg="#f0f4f7").pack(anchor='w')

# --- Generate Button --- #
tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#007acc", fg="white", width=20, command=generate_password).pack(pady=10)

# --- Result Display --- #
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=("Consolas", 14), justify='center', width=32, state='readonly').pack(pady=5)

# --- Strength Display --- #
strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var, font=("Arial", 11, "bold"), fg="green", bg="#f0f4f7").pack(pady=5)

# --- Copy Button --- #
tk.Button(root, text="📋 Copy to Clipboard", font=("Arial", 11), bg="#28a745", fg="white", width=20, command=copy_to_clipboard).pack(pady=10)

# --- Start GUI --- #
root.mainloop()
