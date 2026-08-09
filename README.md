# Password Generator

A clean, modular Python desktop application that allows users to generate secure, randomized passwords with customizable lengths. Built with a focus on simplicity and ease of use.

## Features
*   **Customizable Length:** Choose a password length between 8 and 20 characters.
*   **Complex Character Mix:** Automatically generates a secure blend of:
    *   Uppercase letters
    *   Lowercase letters
    *   Special symbols
*   **Clean GUI:** A native-looking desktop interface built with `tkinter`.
*   **Modular Design:** Separate logic for password generation and user interface, making the codebase easy to maintain and extend.

## Built With
*   [Python 3](https://www.python.org/)
*   [Tkinter](https://tkdocs.com/) (Standard Python GUI Library)
*   [Random](https://docs.python.org/3/library/random.html) (Core Library)

## Prerequisites
Before running the application, ensure you have Python 3.x installed on your system.

## Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Tyler-Adams27/password-generator.git
    cd password-generator
    ```

2.  **Run the application:**
    Navigate to the root directory and run the main entry point:
    ```bash
    python src/main.py
    ```

## Project Structure
```text
.
├── src/
│   ├── main.py           # Entry point of the application
│   ├── user_interface.py # Handles the Tkinter window and UI components
│   └── generator.py      # Contains the core logic for password generation
├── README.md             # Project documentation
└── LICENSE               # Project license
```

## How it Works
*   **`main.py`**: Initializes the `MainWindow` class and starts the application loop.
*   **`user_interface.py`**: Manages the layout, including the password display box, the length slider, and the generate button.
*   **`generator.py`**: Uses a weighted random selection process to pick characters from different pools (uppercase, lowercase, and symbols) based on a random range to ensure variety in every generated password.
