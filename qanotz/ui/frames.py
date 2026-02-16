import tkinter as tk
from qanotz.ui.ui import UIController

class EditorFrame(tk.Frame):
    def __init__(self, master: UIController, **kwargs):
        self.root = tk.Frame(master.root, **kwargs)

        self.label = tk.Label(self.root, text="Welcome to QANotz", font=("Arial", 32))
        self.label.grid(row=0, column=0, padx=10, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, pady=10)

        self.button1 = tk.Button(button_frame, text="Save QA")
        self.button1.pack(side=tk.LEFT, padx=5)

        self.button2 = tk.Button(button_frame, text="Open QA")
        self.button2.pack(side=tk.LEFT, padx=5)

        self.button3 = tk.Button(button_frame, text="Delete QA")
        self.button3.pack(side=tk.LEFT, padx=5)

        self.button_switch = tk.Button(button_frame, text="Switch Mode")
        self.button_switch.pack(side=tk.LEFT, padx=5)

        self.text = tk.Text(self.root, height=10, width=30)
        self.text.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

class MenuFrame(tk.Frame):
    def __init__(self, master: UIController, **kwargs):
        self.root = tk.Frame(master.root, **kwargs)

        self.label = tk.Label(self.root, text="Welcome to QANotz", font=("Arial", 32))
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.create_button = tk.Button(self.root, text="Create New QA")
        self.create_button.grid(row=1, column=0, padx=10, pady=10)

        self.open_button = tk.Button(self.root, text="Open Existing QA")
        self.open_button.grid(row=2, column=0, padx=10, pady=10)

        self.edit_button = tk.Button(self.root, text="Edit QA")
        self.edit_button.grid(row=3, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete QA")
        self.delete_button.grid(row=4, column=0, padx=10, pady=10)

        self.root.grid_columnconfigure(0, weight=1)