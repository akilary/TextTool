import tkinter as tk

from .config import Cfg


class TextTool(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Text Tool")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.cfg = Cfg()

        self._create_menubar()
        self.editor = tk.Text(font=("Arial", 12), undo=True)
        self.editor.grid(row=0, column=0, sticky=tk.NSEW)
        self._create_statusbar()

    def _create_menubar(self) -> None:
        """Создаёт меню-бар"""
        main_menu = tk.Menu(self)

        for menu_name, items in self.cfg.menu_config.items():
            menu = tk.Menu(main_menu, tearoff=False)
            for item in items:
                command_func = self.cfg.command_registry[item["command"]]
                menu.add_command(label=item["label"], command=lambda func=command_func: func(self))
            main_menu.add_cascade(label=menu_name, menu=menu)

        self.config(menu=main_menu)

    def _create_statusbar(self) -> None:
        """"""
        frame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        frame.grid(row=1, column=0, sticky=tk.EW)

        statusbar_text = [
            "Общее количество символов: ",
            "Количество букв: ",
            "Количество слов: ",
            "Количество предложений: ",
            "Средняя длина слова: ",
            "Палиндром: ",
            "Количество гласных: ",
            "Количество согласных: "
        ]

        columns_per_row = 4
        for i, text in enumerate(statusbar_text):
            row = i // columns_per_row
            col = i % columns_per_row
            tk.Label(frame, text=text, font=("Arial", 10)).grid(row=row, column=col, sticky=tk.W, padx=10, pady=5)

        for col in range(columns_per_row):
            frame.grid_columnconfigure(col, weight=1)
