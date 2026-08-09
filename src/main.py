"""
Entry point of the program.
"""
from user_interface import MainWindow

def main():
    """
    Main loop.
    """
    window = MainWindow("Password Generator", "500x500") # Init MainWindow class
    window.show_window() # Show window

if __name__ == "__main__":
    main()
