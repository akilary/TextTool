import tkinter as tk
from tkinter.font import Font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import TextToolApp


class StatusBarView(tk.Frame):
    def __init__(self, root: "TextToolApp"):
        super().__init__(root, relief="sunken", borderwidth=1)
        self.grid(row=1, column=0, sticky="ew")

        self.labels = {}
        columns_per_row = 3

        texts = [
            "Общее количество символов",
            "Количество букв",
            "Количество слов",
            "Количество предложений",
            "Количество гласных",
            "Количество согласных",
        ]
        label_font = Font(family="Consolas", size=10)
        value_color = "#1a1a1a"

        for i, text in enumerate(texts):
            row = i // columns_per_row
            col = i % columns_per_row

            frame = tk.Frame(self, bg="#e6e6e6", padx=5, pady=2)
            frame.grid(row=row, column=col, sticky="we", padx=3, pady=2)

            lbl = tk.Label(frame, text=f"{text}: 0", anchor="w",
                           font=label_font, bg="#e6e6e6", fg=value_color)
            lbl.pack(fill="x")
            self.labels[text] = lbl

        for col in range(columns_per_row):
            self.grid_columnconfigure(col, weight=1)

    def update_val(self, stats: dict[str, int]) -> None:
        """Обновить значения в статусбаре"""
        for key, value in stats.items():
            if key in self.labels:
                self.labels[key].config(text=f"{key}: {value}")
