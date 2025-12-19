from typing import Callable

from models import TextModel, FileModel, EncryptionModel

from .encryption_controller import EncryptionController
from .file_controller import FileController
from .find_controller import FindController
from .statusbar_controller import StatusBarController
from .text_controller import TextController
from views import MainView

class MainController:
    def __init__(self, main_view: MainView):
        self.main_view = main_view

        self.text_model = TextModel()
        self.file_model = FileModel()
        self.encryption_model = EncryptionModel()

        self.encryption_controller = EncryptionController(self.main_view, self.encryption_model, self.text_model)
        self.file_controller = FileController(self.main_view, self.file_model)
        self.find_controller = FindController(self.main_view, self.text_model)
        self.statusbar_controller = StatusBarController(self.main_view, self.text_model)
        self.text_controller = TextController(self.main_view, self.text_model)

    def on_text_change(self, _) -> None:
        """Обрабатывает событие изменения текста (<<Modified>>)."""
        self.statusbar_controller.update()
        try:
            self.main_view.editor.edit_modified(False)
        except Exception as e:
            print(f"Error in MainController: {e}")
            return

    @staticmethod
    def get_menu_structure() -> dict[str, list[str]]:
        """Возвращает структуру меню"""
        return {
            "Файл": ["Открыть TXT/HTML", "Сохранить TXT", "Сохранить как...", "-", "Выход"],
            "Правка": ["Копировать", "Вставить", "Отмена"],
            "Обработка текста": ["Верхний регистр", "Нижний регистр", "Удалить пустые строки",
                                 "Удалить лишние пробелы"],
            "Инструменты": ["Очистить HTML", "Поиск и замена"],
            "Шифрование": ["Зашифровать", "Дешифровать"],
            "Фильтры": ["Оставить только кириллицу", "Оставить только латиницу"],
        }

    def get_actions(self) -> dict[str, Callable[[], None]]:
        """Собирает словарь действий от под-контроллеров"""
        actions = {}
        actions.update(self.encryption_controller.get_actions())
        actions.update(self.file_controller.get_actions())
        actions.update(self.find_controller.get_actions())
        actions.update(self.text_controller.get_actions())
        return actions
