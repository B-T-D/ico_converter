import tkinter as tk
from tkinter import ttk

from . import views as v

class Application(tk.Tk):
    """Application root window."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ICO Converter")

        self.callbacks = {
            'file->select': self.on_file_select,
            'file->quit': self.quit,
            'show_fileslist': self.show_fileslist,
            'new_file': self.open_file,
            'on_open_file': self.open_file,
            'on_save': self.on_save
        }

  
        # File selection list
        self.fileslist = v.FilesList(self, self.callbacks)
        self.fileslist.grid(row=1, padx=10, sticky='NSEW')
        self.populate_fileslist()

    def show_fileslist(self):
        pass
