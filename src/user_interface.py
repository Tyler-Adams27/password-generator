"""
The user interface module.
"""
import tkinter as tk

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
        window_root = tk.Tk()
        window_root.title(self.window_title) # Set window title.
        window_root.geometry(self.window_size) # Set default window size.
        window_root.mainloop() # Main loop of the window.


