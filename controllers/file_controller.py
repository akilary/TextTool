from typing import Callable

from models import FileModel
from views import MainView


class FileController:
    def __init__(self, main_view: MainView, file_model: FileModel):
        self.main_view = main_view
        self.file_model = file_model

    def _open_file(self) -> None:
        """Открывает файл и вставляет в редактор"""
        self.file_model.open_file()
        self.main_view.editor.delete("1.0", "end-1c")
        self.main_view.editor.insert("1.0", self.file_model.get_text())

    def _save_file(self) -> None:
        """Сохраняет текст в файл"""
        self._save(self.file_model.save_file)

    def _save_as(self) -> None:
        """Сохраняет текст в новый файл"""
        self._save(self.file_model.save_as)

    def _save(self, method: Callable[[], None]) -> None:
        """Обновляет модель и вызывает метод сохранения"""
        text = self.main_view.editor.get("1.0", "end-1c")
        self.file_model.set_text(text)
        method()

    def get_actions(self) -> dict[str, Callable[[], None]]:
        """Возвращает доступные действия"""
        return {
            "Открыть TXT/HTML": self._open_file,
            "Сохранить TXT": self._save_file,
            "Сохранить как...": self._save_as,
            "Выход": self.main_view.root.destroy,
        }
