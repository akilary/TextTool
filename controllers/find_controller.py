from typing import Callable

from models import TextModel
from utils import require_view
from views import MainView, FindView


class FindController:
    def __init__(self, main_view: MainView, text_model: TextModel):
        self.main_view = main_view
        self.text_model = text_model
        self.find_view: FindView | None = None

    def _open_view(self) -> None:
        """Открывает окно поиска"""
        if self.find_view and self.find_view.winfo_exists():
            self.find_view.lift()
            return

        self.find_view = FindView(self.main_view.root)

        self.find_view.find_button.config(command=self._find)
        self.find_view.clear_button.config(command=self._clear)
        self.find_view.replace_check.config(command=self._toggle_replace)
        self.find_view.protocol("WM_DELETE_WINDOW", self._close)

    @require_view("find_view")
    def _find(self) -> None:
        """Выполняет поиск текста"""
        query = self.find_view.entry_search.get()
        if not query:
            self.find_view.result_label.config(text="Введите запрос")
            return

        text = self.main_view.editor.get("1.0", "end-1c")
        self.text_model.set_text(text)

        match_case = self.find_view.match_case_var.get()
        use_regex = self.find_view.regex_var.get()
        positions = self.text_model.find_positions(query, match_case, use_regex)

        self._highlight(positions)
        self.find_view.result_label.config(text=f"Совпадений: {len(positions)}")

        if self.find_view.enable_replace_var.get(): self._replace()

    @require_view("find_view")
    def _replace(self) -> None:
        """Заменяет найденный текст"""
        text = self.main_view.editor.get("1.0", "end-1c")
        self.text_model.set_text(text)

        new_text = self.text_model.replace_text(
            self.find_view.entry_search.get(),
            self.find_view.entry_replace.get(),
            self.find_view.match_case_var.get(),
            self.find_view.regex_var.get()
        )

        self.main_view.editor.delete("1.0", "end")
        self.main_view.editor.insert("1.0", new_text)

    def _highlight(self, positions: list[tuple[str, str]]) -> None:
        """Подсвечивает совпадения"""
        self.main_view.editor.tag_remove("search_highlight", "1.0", "end")
        for start, end in positions:
            self.main_view.editor.tag_add("search_highlight", start, end)

    def _clear(self) -> None:
        """Очищает подсветку"""
        self.main_view.editor.tag_remove("search_highlight", "1.0", "end")
        if self.find_view:
            self.find_view.result_label.config(text="Совпадений: 0")

    @require_view("find_view")
    def _toggle_replace(self) -> None:
        """Включает/выключает режим замены"""
        enabled = self.find_view.enable_replace_var.get()
        self.find_view.entry_replace.config(state="normal" if enabled else "disabled")
        self.find_view.find_button.configure(text="Найти + Заменить" if enabled else "Найти")

    def _close(self) -> None:
        """Закрывает окно поиска"""
        self._clear()
        if self.find_view:
            self.find_view.destroy()
            self.find_view = None

    def get_actions(self) -> dict[str, Callable[[], None]]:
        """Возвращает доступные действия"""
        return {
            "Поиск и замена": self._open_view,
        }
