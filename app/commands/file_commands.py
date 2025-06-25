import tkinter as tk
from tkinter import filedialog

from .utils import get_editor_text, set_editor_text


def open_file(r) -> None:
    """Открывает файлы формата .txt и .html"""
    filepath = tk.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("HTML Files", "*.html")])
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            set_editor_text(r, text)


def save_file(r) -> None:
    """Сохраняет файл в формате .txt"""
    filepath = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")], initialfile="my_file.txt")
    if filepath != "":
        text = get_editor_text(r)
        with open(filepath, "w") as file:
            file.write(text)


def save_as(r) -> None:
    """Сохраняет в произвольном формате"""
    filepath = filedialog.asksaveasfilename(filetypes=[("All Files", "*.*")], initialfile="my_file")
    if filepath != "":
        text = get_editor_text(r)
        with open(filepath, "w") as file:
            file.write(text)


def close_app(r) -> None:
    """Закрывает приложение"""
    r.destroy()
