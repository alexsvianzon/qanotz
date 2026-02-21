import tkinter as tk
from enum import Enum
from qanotz.ui.frames import *

class Frames(Enum):
    MENU = 1
    VIEW = 2
    EDITOR = 3
    SEARCH = 4

class UIController:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.prev_frame: Frames = Frames.MENU
        self.current_frame: Frames = Frames.MENU

        ListboxFrame(self).root.pack(fill=tk.BOTH, expand=True)

    def switch_frame(self, frame_enum: Frames):
        self.prev_frame = self.current_frame
        self.current_frame = frame_enum

        for widget in self.root.winfo_children():
            widget.destroy()

        match frame_enum:
            case Frames.MENU:
                frame_class = MenuFrame
            case Frames.VIEW:
                frame_class = ViewFrame
            case Frames.EDITOR:
                frame_class = EditorFrame
            case Frames.SEARCH:
                frame_class = SearchFrame
            case _:
                raise ValueError(f"Invalid frame enum: {frame_enum}")

        frame_class(self).root.pack(fill=tk.BOTH, expand=True)