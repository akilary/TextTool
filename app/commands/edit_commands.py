import pyperclip

from .utils import get_editor_text, set_editor_text
from ..types import App


def copy_text(app: App) -> None:
    """Копирует текст в буфер обмена из редактора"""
    pyperclip.copy(get_editor_text(app))


def paste_text(app: App) -> None:
    """Вставляет текст из буфера обмена в редактор"""
    set_editor_text(app, pyperclip.paste())


def undo_text(app: App) -> None:
    """Отменяет последнее действие"""
    app.editor.edit_undo()
