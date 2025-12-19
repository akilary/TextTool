from typing import Callable

from models import TextModel
from views import MainView


class TextController:
    def __init__(self, main_view: MainView, text_model: TextModel):
        self.main_view = main_view
        self.text_model = text_model

    def _copy_text(self) -> None:
        """Копирует текст в буфер"""
        text = self.main_view.editor.get("1.0", "end-1c")
        self.text_model.set_text(text)
        self.text_model.copy()

    def _paste_text(self) -> None:
        """Вставляет текст из буфера"""
        self.text_model.paste()
        self._insert_text()

    def _apply(self, func: Callable[[], None]) -> None:
        """Применяет функцию к тексту и обновляет редактор"""
        text = self.main_view.editor.get("1.0", "end-1c")
        self.text_model.set_text(text)
        func()
        self._insert_text()

    def _insert_text(self) -> None:
        """Обновляет редактор содержимым модели"""
        self.main_view.editor.delete("1.0", "end-1c")
        self.main_view.editor.insert("1.0", self.text_model.get_text())

    def get_actions(self) -> dict[str, Callable[[], None]]:
        """Возвращает доступные действия"""
        return {
            "Копировать": self._copy_text,
            "Вставить": self._paste_text,
            "Отмена": self.main_view.editor.edit_undo,
            "Верхний регистр": lambda: self._apply(self.text_model.to_uppercase),
            "Нижний регистр": lambda: self._apply(self.text_model.to_lowercase),
            "Удалить пустые строки": lambda: self._apply(self.text_model.remove_empty_lines),
            "Удалить лишние пробелы": lambda: self._apply(self.text_model.remove_extra_spaces),
            "Очистить HTML": lambda: self._apply(self.text_model.clean_html),
            "Оставить только кириллицу": lambda: self._apply(self.text_model.only_cyrillic),
            "Оставить только латиницу": lambda: self._apply(self.text_model.only_latin),
        }
