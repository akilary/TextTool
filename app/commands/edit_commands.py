import pyperclip

from .utils import get_editor_text, set_editor_text


def copy_text(r) -> None:
    """Копирует текст в буфер обмена из редактора"""
    pyperclip.copy(get_editor_text(r))


def paste_text(r) -> None:
    """Вставляет текст из буфера обмена в редактор"""
    set_editor_text(r, pyperclip.paste())


def undo_text(r) -> None:
    """Отменяет последнее действие"""
    r.editor.edit_undo()
