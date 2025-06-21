import tkinter as tk

from .config import MENU_CONFIG


class TextTool(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Text Tool")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self._create_menubar()
        tk.Text(font=("Arial", 12)).grid(row=0, column=0, sticky=tk.NSEW)
        self._create_statusbar()

    def _create_menubar(self) -> None:
        """Создаёт меню-бар"""
        main_menu = tk.Menu(self)

        for menu_name, items in MENU_CONFIG.items():
            menu = tk.Menu(main_menu, tearoff=False)
            for item in items:
                menu.add_command(label=item["label"])
            main_menu.add_cascade(label=menu_name, menu=menu)

        self.config(menu=main_menu)

    def _create_statusbar(self) -> None:
        """"""
        frame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        frame.grid(row=1, column=0, sticky=tk.EW)

        statusbar_text = [
            "Общее количество символов: 170",
            "Количество букв: 141",
            "Количество слов: 12",
            "Количество предложений: 6",
            "Средняя длина слова: 7",
            "Палиндром: Нет",
            "Количество гласных: 35",
            "Количество согласных: 22"
        ]

        columns_per_row = 4
        for i, text in enumerate(statusbar_text):
            row = i // columns_per_row
            col = i % columns_per_row
            tk.Label(frame, text=text, font=("Arial", 10)).grid(row=row, column=col, sticky=tk.W, padx=10, pady=5)

        for col in range(columns_per_row):
            frame.grid_columnconfigure(col, weight=1)
