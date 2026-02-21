from __future__ import annotations

import tkinter as tk
from typing import TYPE_CHECKING
import sys
from qanotz.data.data import DatabaseManagerInstance

if TYPE_CHECKING:
    from qanotz.ui.ui import UIController, Frames

class Frame(tk.Frame):
    def __init__(self, master: UIController, **kwargs):
        # from qanotz.ui.ui import UIController
        self.root = tk.Frame(master.root, **kwargs)
        self.uimaster: UIController = master

    def switch_to(self, frame_enum: Frames):
        self.uimaster.switch_frame(frame_enum)

class EditorFrame(Frame): # DONE: Can switch from editor to view or search, as well as having buttons for saving and deleting QAs. Must handle going to a save frame if it is a new file.
    def __init__(self, master: UIController, **kwargs):
        from qanotz.ui.ui import Frames
        super().__init__(master, **kwargs)

        self.db = DatabaseManagerInstance()

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, pady=10)

        self.switch_button = tk.Button(button_frame, text="View QA", command=lambda: self.switch_to(Frames.VIEW))
        self.switch_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(button_frame, text="Save QA", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(button_frame, text="Delete QA")
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.open_button = tk.Button(button_frame, text="Open QA", command=lambda: self.switch_to(Frames.SEARCH))
        self.open_button.pack(side=tk.LEFT, padx=5)

        self.text = tk.Text(self.root, height=10, width=30)
        self.text.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def save_file(self):
        from qanotz.ui.ui import Frames
        if self.uimaster.prev_frame == Frames.MENU:
            self.db.create_qafile(self.text.get("1.0", "end"))

class MenuFrame(Frame): # Can switch to edito (new) or search
    def __init__(self, master: UIController, **kwargs):
        from qanotz.ui.ui import Frames
        super().__init__(master, **kwargs)

        self.label = tk.Label(self.root, text="Welcome to QANotz", font=("Arial", 32))
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.create_button = tk.Button(self.root, text="Create New QA", command=lambda: self.switch_to(Frames.EDITOR))
        self.create_button.grid(row=1, column=0, padx=10, pady=10)

        self.open_button = tk.Button(self.root, text="Open Existing QA", command=lambda: self.switch_to(Frames.SEARCH))
        self.open_button.grid(row=2, column=0, padx=10, pady=10)

        self.root.grid_columnconfigure(0, weight=1)

class ViewFrame(Frame): # Can switch to editor or search, as well as deleteing the current QA and going to the menu.
    def __init__(self, master: UIController, **kwargs):
        from qanotz.ui.ui import Frames
        super().__init__(master, **kwargs)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, pady=10)

        self.edit_button = tk.Button(button_frame, text="Edit QA", command=lambda: self.switch_to(Frames.EDITOR))
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.open_button = tk.Button(button_frame, text="Open QA", command=lambda: self.switch_to(Frames.SEARCH))
        self.open_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(button_frame, text="Delete QA")
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.text = tk.Text(self.root, height=10, width=30)
        self.text.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

class SearchFrame(Frame):
    def __init__(self, master: UIController, **kwargs):
        from qanotz.ui.ui import Frames
        super().__init__(master, **kwargs)

        self.database = DatabaseManagerInstance()

        self.search = tk.StringVar()
        self.search_entry = tk.Entry(self.root, textvariable=self.search, width=30)
        self.search_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.search_button = tk.Button(self.root, text="Search", command=self.search_all_files)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1, column=0, pady=10)

        self.edit_button = tk.Button(self.button_frame, text="Edit QA")
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.open_button = tk.Button(self.button_frame, text="Open QA")
        self.open_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete QA")
        self.delete_button.pack(side=tk.LEFT, padx=5)

        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)

        self.selected = tk.StringVar()
        self.selector_frame = tk.Frame(canvas)

        # Keep canvas scrollregion in sync with the selector_frame size
        self.selector_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a window on the canvas and keep a handle so we can resize it
        self.canvas_window = canvas.create_window((0, 0), window=self.selector_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack canvas + scrollbar inside their container frame
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Place the container frame into the root using grid so it expands
        frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Make inner window match canvas width when the canvas is resized
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(self.canvas_window, width=e.width))

        # Mouse wheel scrolling helpers so the user can scroll anywhere over
        # the selector area (not only the scrollbar).
        def _on_mousewheel(event):
            try:
                # Linux: Button-4 (up), Button-5 (down)
                if hasattr(event, 'num') and event.num in (4, 5):
                    if event.num == 4:
                        canvas.yview_scroll(-1, 'units')
                    else:
                        canvas.yview_scroll(1, 'units')
                    return
                # Windows / macOS: use event.delta sign
                if hasattr(event, 'delta'):
                    if event.delta < 0:
                        canvas.yview_scroll(1, 'units')
                    elif event.delta > 0:
                        canvas.yview_scroll(-1, 'units')
            except Exception:
                pass

        def _bind_to_mousewheel(event=None):
            if sys.platform.startswith('linux'):
                canvas.bind_all('<Button-4>', _on_mousewheel)
                canvas.bind_all('<Button-5>', _on_mousewheel)
            else:
                canvas.bind_all('<MouseWheel>', _on_mousewheel)

        def _unbind_from_mousewheel(event=None):
            if sys.platform.startswith('linux'):
                canvas.unbind_all('<Button-4>')
                canvas.unbind_all('<Button-5>')
            else:
                canvas.unbind_all('<MouseWheel>')

        # Bind enter/leave on both the canvas and the selector frame so
        # scrolling works when hovering over any child (radiobuttons, etc.)
        self.selector_frame.bind('<Enter>', _bind_to_mousewheel)
        self.selector_frame.bind('<Leave>', _unbind_from_mousewheel)
        canvas.bind('<Enter>', _bind_to_mousewheel)
        canvas.bind('<Leave>', _unbind_from_mousewheel)

        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def search_all_files(self):
        results = self.database.search_qas(self.search.get())

        for widget in self.selector_frame.winfo_children():
            widget.destroy()

        for result in results:
            (label, file_name) = result

            rb = tk.Radiobutton(self.selector_frame, text=label, variable=self.selected, value=file_name)
            rb.pack(side=tk.TOP, anchor='w')

class ListboxFrame(Frame):
    def __init__(self, master: UIController, **kwargs):
        super().__init__(master, **kwargs)

        import random

        choices = [random.randint(1, 100) for _ in range(100)]
        choicesvar = tk.StringVar(value=choices)
        l = tk.Listbox(self.root, listvariable=choicesvar)
        l.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Make the listbox expand with the frame
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.listbox = l
