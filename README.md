# Random-Password-Generator

**Introduction:**
This Python script uses the Tkinter library to create a simple graphical user interface (GUI) for generating passwords. The application allows users to specify the length of the password and generates a random password based on the specified length.

**Code Explanation:**

1. **Importing Libraries:**
   - `tkinter`: Used for creating the GUI.
   - `messagebox`: Used for displaying error messages.
   - `string` and `random`: Used for generating random passwords.

2. **Password Generation Function (`generate_password`):**
   - This function generates a random password of the specified length.
   - It combines lowercase letters, uppercase letters, digits, and special characters to create a pool of characters.
   - It ensures that the generated password contains at least one character from each character set.
   - It then fills the remaining length of the password with random choices from the combined character set.
   - Finally, it shuffles the characters and joins them into a string to form the final password.

3. **Event Handler Function (`on_generate_password`):**
   - This function is called when the "Generate Password" button is clicked.
   - It retrieves the password length entered by the user from the entry widget (`entry_length`).
   - It generates a password using the `generate_password` function.
   - If the password length is less than 4 characters, it raises a `ValueError` with an appropriate message.
   - If a `ValueError` is raised, it displays an error message using `messagebox.showerror`.
   - Otherwise, it clears the previous password (if any) from the password entry widget (`entry_password`) and inserts the generated password into the widget.

4. **Creating the Main Window (`root`):**
   - The main window is created using `tk.Tk()`.
   - The title of the window is set to "Password Generator" using `root.title`.
   - The geometry of the window is set to "400x200" using `root.geometry`.

5. **Creating and Placing Widgets:**
   - Labels (`label_length`, `label_password`) are created to provide instructions and display the generated password.
   - Entry widgets (`entry_length`, `entry_password`) are created for user input and displaying the generated password.
   - Button widget (`btn_generate`) is created for triggering the password generation process.
   - Widgets are packed using the `pack` method to place them in the window.

6. **Main Loop:**
   - The `root.mainloop()` function starts the event loop, allowing the GUI to respond to user interactions.

**Conclusion:**
This Python script demonstrates how to create a simple password generator GUI using Tkinter. Users can specify the length of the password, and the application generates a random password accordingly. Error handling is implemented to handle invalid user input. Overall, this application provides a user-friendly way to generate strong passwords.
