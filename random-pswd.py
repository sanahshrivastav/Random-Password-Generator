import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        # Get the length of the password from the entry widget
        length = int(length_entry.get())

        # Ensure the length is at least 4 characters
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters.")
            return

        # Define the character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        # Combine all character sets
        all_chars = lower + upper + digits + special

        # Ensure the password contains at least one character from each set
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special)
        ]

        # Fill the remaining length of the password with random choices from all character sets
        password += random.choices(all_chars, k=length-4)

        # Shuffle the resulting list to ensure randomness
        random.shuffle(password)

        # Join the list into a string to form the final password
        generated_password.set(''.join(password))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Length Label
length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

# Length Entry
length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "12")  # Default length

# Generate Button
generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, columnspan=2, padx=5, pady=5)

# Generated Password Label
generated_password = tk.StringVar()
generated_password_label = tk.Label(frame, textvariable=generated_password)
generated_password_label.grid(row=2, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
