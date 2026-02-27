"""
Source code file for QANotz.
This file contains the main application class and the entry point to run the app.
"""

import tkinter as tk
from qanotz.ui.ui import UIController
from qanotz.data.data import DatabaseManagerInstance

class App:
    def __init__(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title("QANotz")
        self.root.geometry("500x400")

        self.database: DatabaseManagerInstance = DatabaseManagerInstance()

        self.ui_controller: UIController = UIController(self)
    
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()