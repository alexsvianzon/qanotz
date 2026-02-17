import tkinter as tk

class UIController:
    def __init__(self, app):
        from qanotz.ui import frames as frames

        self.app = app
        self.root = app.root

        frames.ViewFrame(self).root.pack(fill=tk.BOTH, expand=True)
