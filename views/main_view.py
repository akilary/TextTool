import tkinter as tk
from tkinter.font import Font
from typing import TYPE_CHECKING

from .statusbar_view import StatusBarView

if TYPE_CHECKING:
    from app import TextToolApp


class MainView:
    def __init__(self, root: "TextToolApp"):
        self.root = root

        self.editor = tk.Text(
            self.root,
            undo=True,
            wrap="word",
            font=Font(family="Consolas", size=12),
            fg="#222222",
            insertbackground="#000000",
            selectbackground="#a0c4f1",
            relief="flat",
            padx=5, pady=5
        )
        self.editor.grid(row=0, column=0, sticky="nsew")
        self.editor.tag_config("search_highlight", background="yellow")

        self.statusbar = StatusBarView(self.root)
