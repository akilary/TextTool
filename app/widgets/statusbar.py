import tkinter as tk

# TODO: Заглушка
def create_statusbar(r) -> None:
    """Создаёт статус-бар"""
    cfg = r.cfg
    frame = tk.Frame(r, bd=1, relief=tk.SUNKEN)
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
        tk.Label(frame, text=text, font=(cfg.FONT_NAME, 10)).grid(row=row, column=col, sticky=tk.W, padx=10, pady=5)

    for col in range(columns_per_row):
        frame.grid_columnconfigure(col, weight=1)
