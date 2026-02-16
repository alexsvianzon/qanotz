"""
Source code file for my basic notes app using Tkinter.
This file manages the database operations for the notes app.
This includes creating the database, adding, retrieving, updating, and deleting notes.
"""

from ..utils import os as os_utils

class Database:
    def __init__(self):
        # get appdata directory for the notes app
        appdata_dir = os_utils.get_appdata_dir()
        self.db_path = f"{appdata_dir}/notes_app"

        # check if the database directory exists or create it
        os_utils.ensure_dir(self.db_path)

if __name__ == "__main__":
    db = Database()
    print(f"Database initialized at: {db.db_path}")
