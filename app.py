import tkinter as tk
from views import MainView, MenuBuilder
from controllers import MainController


class TextToolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Работа с текстом")
        self.iconbitmap("icons/icon.ico")

        self.geometry("800x600")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_view = MainView(self)
        self.controller = MainController(self.main_view)

        actions = self.controller.get_actions()
        menu_structure = self.controller.get_menu_structure()
        self.menu = MenuBuilder(self, menu_structure, actions)

        self.main_view.editor.bind("<<Modified>>", self.controller.on_text_change)
