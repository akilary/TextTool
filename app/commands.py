import tkinter as tk
from tkinter import filedialog

import pyperclip


def open_file(r) -> None:
    """Открывает файлы формата .txt и .html"""
    filepath = tk.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("HTML Files", "*.html")])
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            r.editor.delete("1.0", tk.END)
            r.editor.insert("1.0", text)


def save_file(r) -> None:
    """Сохраняет файл в формате .txt"""
    filepath = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")], initialfile="my_file.txt")
    if filepath != "":
        text = r.editor.get("1.0", tk.END)
        with open(filepath, "w") as file:
            file.write(text)


def save_as(r) -> None:
    """Сохраняет в произвольном формате"""
    filepath = filedialog.asksaveasfilename(filetypes=[("All Files", "*.*")], initialfile="my_file")
    if filepath != "":
        text = r.editor.get("1.0", tk.END)
        with open(filepath, "w") as file:
            file.write(text)


def close_app(r) -> None:
    """Закрывает приложение"""
    r.destroy()


def copy_text(r) -> None:
    """Копирует текст в буфер обмена"""
    pyperclip.copy(r.editor.get("1.0", tk.END))


def insert_text(r) -> None:
    """Вставляет текст из буфера обмена"""
    r.editor.delete("1.0", tk.END)
    r.editor.insert("1.0", pyperclip.paste())


def undo_text(r) -> None:
    """Отменяет последнее действие"""
    r.editor.edit_undo()


def remove_empty_lines(r) -> None:
    """Удаляет пустые строки"""
    text_lines = r.editor.get("1.0", tk.END).splitlines()
    formated_text = "\n".join([line for line in text_lines if line])
    r.editor.delete("1.0", tk.END)
    r.editor.insert("1.0", formated_text)


def remove_extra_spaces(r) -> None:
    """Удаляет лишние пробелы в строке"""
    text = r.editor.get("1.0", tk.END)
    while "  " in text:
        text = text.replace("  ", " ")
    formated_text = "\n".join([line.rstrip() for line in text.splitlines()])
    r.editor.delete("1.0", tk.END)
    r.editor.insert("1.0", formated_text)
