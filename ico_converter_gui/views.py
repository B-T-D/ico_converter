import tkinter as tk
from tkinter import ttk

class FilesList(tk.Frame):
    """Display for image files available for conversion to .ico."""

    column_schema = {
        'Name': {'label': 'Name', 'stretch': True},
        'Modified': {'label': 'Date Modified'},
        'Type': {'label': 'File Type'}
        }
    default_width = 100
    default_minwidth = 10
    default_anchor = tk.CENTER

    def __init__(self, parent, callbacks, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.callbacks = callbacks
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Create treeview
        self.treeview = ttk.Treeview(
            self,
            columns=list(self.column_defs.keys())[1:],
            selectmode='browse'
        )

        # Create and configure scrollbar for treeview
        self.scrollbar = ttk.Scrollbar(
            self,
            orient=tk.VERTICALm
            command=self.treeview.yview
        )
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.treeview.grid(row=0, column=0, sticky='NSEW')
        self.scrollbar.grid(row=0, column=1, sticky='NSW')

        # Configure treeview columns
        for name, definition in self.column_schema.items():
            label = definition.get('label', '')
            stretch = definition.get('stretch', False)
            self.treeview.heading(name, text=label)
            self.treeview.column(name, stretch=stretch)

        self.treeview.bind('<<TreeviewOpen>>', self.on_open_file)

    def populate(self, rows):
        """Clear the treeview and write the supplied data rows to it."""

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        valuekeys = list(self.column_schema.keys())[1:]
        for rownum, rowdata in enumerate(rows):
            values = [rowdata[key] for key in valuekeys]
            self.treeview.insert('', 'end', iid=str(rownum), text=str(rownum),
                                 values=values)

        if len(rows) > 0:
            self.treeview.focus_set()
            self.treeview.selection_set(0)
            self.treeview.focus('0')

    def on_open_file(self, *args):

        selected_id = self.treeview.selection()[0]
        self.callbacks['on_open_record'](selected_id)
