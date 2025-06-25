import tkinter as tk


def get_editor_text(r) -> str:
    """Возвращает текст из редактора"""
    return r.editor.get("1.0", tk.END)


def set_editor_text(r, text: str) -> None:
    """Меняет текст в редакторе"""
    r.editor.delete("1.0", tk.END)
    r.editor.insert("1.0", text.strip())
