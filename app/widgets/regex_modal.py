import re
import tkinter as tk

from ..types import App


# TODO: Добавить чекбокс "Учитывать регистр" для поиска (Match Case)
# TODO: Отображать количество найденных совпадений под полем поиска
# TODO: Показать уведомление, если совпадений не найдено (например, label или messagebox)
class RegexModal(tk.Toplevel):
    def __init__(self, master: App):
        super().__init__(master)
        self.cfg = master.cfg

        self.title("Поиск и замена (RegEx)")
        self._center_modal()
        self.resizable(False, False)

        self.columnconfigure(1, weight=1)

        self.text_editor = master.editor

        tk.Label(self, text="Поиск:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.search_entr = tk.Entry(self)
        self.search_entr.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky=tk.EW)

        tk.Label(self, text="Заменить:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.replace_entr = tk.Entry(self, state=tk.DISABLED)
        self.replace_entr.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)

        self.enabled = tk.BooleanVar()
        self.check = tk.Checkbutton(self, text="Вкл", variable=self.enabled, command=self._toggle_replace)
        self.check.grid(row=1, column=2, padx=5)

        self.search_btn = tk.Button(self, text="Найти", width=20, command=self._search_core)
        self.search_btn.grid(row=2, column=0, columnspan=3, pady=15)

        self.clear_selections_btn = tk.Button(self, text="Очистить выделения", width=20,
                                              command=lambda: self.text_editor.tag_remove("found", "1.0", tk.END))
        self.clear_selections_btn.grid(row=3, column=0, columnspan=3, pady=15)

    def _center_modal(self):
        """Задаёт размеры модального окна и центрирует его"""
        w, h = self.cfg.MODAL_WIDTH, self.cfg.MODAL_HEIGHT

        master_x = self.master.winfo_rootx()
        master_y = self.master.winfo_rooty()
        master_width = self.master.winfo_width()
        master_height = self.master.winfo_height()

        x = master_x + (master_width // 2) - (w // 2)
        y = master_y + (master_height // 2) - (h // 2)

        self.geometry(f"{w}x{h}+{x}+{y}")

    def _toggle_replace(self):
        """Переключение режима замены"""
        if self.enabled.get():
            self.replace_entr.configure(state=tk.NORMAL)
            self.search_btn.configure(text="Найти и заменить", command=lambda: self._search_core(True))
        else:
            self.replace_entr.configure(state=tk.DISABLED)
            self.search_btn.configure(text="Найти", command=self._search_core)

    def _search_core(self, replace: bool = False) -> None:
        """Универсальный поиск с возможной заменой"""
        self.text_editor.tag_remove("found", "1.0", tk.END)

        pattern = self.search_entr.get()
        if not pattern: return

        text = self.text_editor.get("1.0", tk.END)
        matches = []

        if self._is_regex():
            try:
                for match in re.finditer(pattern, text, flags=re.IGNORECASE):
                    start = f"1.0+{match.start()}c"
                    end = f"1.0+{match.end()}c"
                    matches.append((start, end, match.group()))
            except re.error:
                return
        else:
            index = "1.0"
            while True:
                index = self.text_editor.search(pattern, index, nocase=1, stopindex=tk.END)
                if not index: break

                end_index = f"{index}+{len(pattern)}c"
                matches.append((index, end_index, pattern))
                index = end_index

        for start, end, match_text in matches:
            if replace:
                self.text_editor.delete(start, end)
                self.text_editor.insert(start, self.replace_entr.get())
                end = f"{start}+{len(self.replace_entr.get())}c"

            self.text_editor.tag_add("found", start, end)

        self.text_editor.tag_config("found", foreground="blue")
        self.search_entr.focus_set()

    def _is_regex(self) -> bool:
        """Проверка на корректную регулярку"""
        try:
            re.compile(self.search_entr.get())
            return True
        except re.error:
            return False
