"""
Source code file for QANotz.
This file contains the main application class and the entry point to run the app.
"""

import tkinter as tk
from qanotz.data.data import Database
from qanotz.ui.ui import UIController

TESTING_MODE = True

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("QANotz")
        self.root.geometry("500x500")

        icon_image = tk.PhotoImage(file='icon.png')
        self.root.iconphoto(False, icon_image)

        self.database = Database()

        self.ui_controller = UIController(self)
    
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()