from models import TextModel
from views import MainView


class StatusBarController:
    def __init__(self, main_view: MainView, text_model: TextModel):
        self.main_view = main_view
        self.text_model = text_model

    def update(self) -> None:
        """Обновляет статусбар на основе текста из редактора"""
        text = self.main_view.editor.get("1.0", "end-1c")
        self.text_model.set_text(text)
        stats = self.text_model.get_stats()

        self.main_view.statusbar.update_val(stats)
