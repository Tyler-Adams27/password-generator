"""
The user interface module.
"""
import tkinter as tk
from generator import generate

class MainWindow():
    """
    The main window class. This will be shown to the user upon opening the program.
    """
    def __init__(self, window_title, window_size):
        """
        Init class variables
        """
        self.window_title = window_title # Window title.
        self.window_size = window_size # Window size.

    def show_window(self):
        """
        Init the window and show it
        """
        window_root = tk.Tk()
        window_root.resizable(False,False) # Make window static
        window_root.title(self.window_title) # Set window title.
        window_root.geometry(self.window_size) # Set default window size.
        result = tk.Entry(window_root)
        result["state"] = "readonly"
        result.place(relx=0.5, rely=0.4, anchor="center")
        generate_button = tk.Button(window_root, text="Generate", width=20, command=lambda:
        generate(letter_count.get(), result))
        generate_button.place(relx=0.5, rely=0.5, anchor="center")
        letter_count = tk.Scale(window_root, from_=8, to=16, orient="horizontal")
        letter_count.place(relx=0.5, rely=0.6, anchor="center")
        window_root.mainloop() # Main loop of the window.

    def pylint_pleaser(self):
        """
        This is to make pylint happy (A class needs two functions for it to be happy)
        """
        print("Happy now?")
