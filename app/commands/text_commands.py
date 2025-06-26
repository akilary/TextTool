import re
from html import unescape

from .utils import get_editor_text, set_editor_text


def remove_empty_lines(r) -> None:
    """Удаляет пустые строки"""
    text_lines = get_editor_text(r).splitlines()
    formated_text = "\n".join([line for line in text_lines if line])
    set_editor_text(r, formated_text)


def remove_extra_spaces(r) -> None:
    """Удаляет лишние пробелы в строке"""
    text = get_editor_text(r)
    formated_text = re.sub(r" +", " ", text)
    formated_text = re.sub(r"^ +| +$", "", formated_text, flags=re.MULTILINE)
    set_editor_text(r, formated_text)


def to_uppercase(r) -> None:
    """Приводит текст в верхний регистр"""
    text = get_editor_text(r)
    set_editor_text(r, text.upper().strip())


def to_lowercase(r) -> None:
    """Приводит текст в нижний регистр"""
    text = get_editor_text(r)
    set_editor_text(r, text.lower().strip())


def clean_html(r) -> None:
    """Очищает текст от HTML тегов и атрибутов"""
    text = get_editor_text(r)
    formated_text = unescape(re.sub("<[^<]+?>", "", text))
    set_editor_text(r, formated_text)
