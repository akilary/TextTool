import tkinter as tk
from ..types import App

def get_editor_text(app: App) -> str:
    """Возвращает текст из редактора"""
    return app.editor.get("1.0", tk.END)


def set_editor_text(app: App, text: str) -> None:
    """Меняет текст в редакторе"""
    app.editor.delete("1.0", tk.END)
    app.editor.insert("1.0", text.strip())
