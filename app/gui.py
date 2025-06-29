import tkinter as tk

from .config import Cfg
from .widgets import create_menubar, create_statusbar


class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.cfg = Cfg()

        self.title("Text Tool")
        self._center_window()
        self.resizable(width=False, height=False)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.editor = tk.Text(font=(self.cfg.FONT_NAME, 12), undo=True, wrap=tk.WORD)
        self.editor.grid(row=0, column=0, sticky=tk.NSEW)

        create_menubar(self)
        create_statusbar(self)

    def _center_window(self) -> None:
        """Задаёт размеры окна и центрируя его"""
        w, h = self.cfg.SCREEN_WIDTH, self.cfg.SCREEN_HEIGHT
        screen_w, screen_h = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (screen_w - w) // 2
        y = (screen_h - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")
