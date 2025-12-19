import tkinter as tk

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import TextToolApp


class FindView(tk.Toplevel):
    def __init__(self, root: "TextToolApp"):
        super().__init__(root)
        self.root = root

        self.title("Поиск и замена")
        self.resizable(False, False)

        tk.Label(self, text="Поиск:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_search = tk.Entry(self, width=30)
        self.entry_search.grid(row=0, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        tk.Label(self, text="Замена:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_replace = tk.Entry(self, width=30, state="disabled")
        self.entry_replace.grid(row=1, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        self.match_case_var = tk.BooleanVar()
        self.regex_var = tk.BooleanVar()
        self.enable_replace_var = tk.BooleanVar(value=False)

        tk.Checkbutton(self, text="Учитывать регистр", variable=self.match_case_var).grid(row=2, column=0, sticky="w",
                                                                                          padx=5)
        tk.Checkbutton(self, text="Использовать регулярку", variable=self.regex_var).grid(row=2, column=1, sticky="w",
                                                                                          padx=5)

        self.replace_check = tk.Checkbutton(self, text="Включить замену", variable=self.enable_replace_var)
        self.replace_check.grid(row=2, column=2, sticky="w", padx=5)

        self.find_button = tk.Button(self, text="Найти")
        self.find_button.grid(row=3, column=0, padx=5, pady=5, sticky="we")

        self.clear_button = tk.Button(self, text="Очистить выделение")
        self.clear_button.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        self.result_label = tk.Label(self, text="Совпадений: 0")
        self.result_label.grid(row=4, column=0, columnspan=4, pady=5)

        self.columnconfigure(1, weight=1)
