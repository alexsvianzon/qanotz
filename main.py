"""

Source code for my basic notes app using Tkinter.
This file contains the main application class and the entry point to run the app.

"""

from tkinter import *
from tkinter import ttk

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Notes App")
        self.root.geometry("400x300")

        self.label = Label(self.root, text="Hello, Tkinter!")
        self.label.pack(pady=20)
    
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()