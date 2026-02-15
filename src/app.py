"""
Source code file for my basic notes app using Tkinter.
This file contains the main application class and the entry point to run the app.
"""

import tkinter as tk
import data.data as dbutils

TESTING_MODE = True

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Notes App")
        self.root.geometry("400x300")

        self.database = dbutils.Database()

        self.label = tk.Label(self.root, text="Hello, Tkinter!")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.text = tk.Text(self.root, height=10, width=30)
        self.text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        if TESTING_MODE:
            print("Testing mode is ON. Initialization complete.")
    
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()