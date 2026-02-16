"""
Source code file for QANotz.
This file contains the main application class and the entry point to run the app.
"""

import tkinter as tk
import data.data as dbutils
import ui.ui as ui

TESTING_MODE = True

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("QANotz")
        self.root.geometry("500x500")

        self.database = dbutils.Database()

        ui.UI(self)
    
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()