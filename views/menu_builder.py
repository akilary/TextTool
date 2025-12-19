import tkinter as tk
from typing import Callable

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import TextToolApp


class MenuBuilder:
    def __init__(self, root: "TextToolApp", menu_structure: dict[str, list[str]], actions: dict[str, Callable]):
        self.menubar = tk.Menu(root)
        root.config(menu=self.menubar)

        for menu_name, items in menu_structure.items():
            menu = tk.Menu(self.menubar, tearoff=0)
            for label in items:
                if label == "-":
                    menu.add_separator()
                else:
                    func = actions.get(label)
                    if func is None:
                        menu.add_command(label=label, state="disabled")
                    else:
                        menu.add_command(label=label, command=func)
            self.menubar.add_cascade(label=menu_name, menu=menu)
