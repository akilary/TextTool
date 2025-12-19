import tkinter as tk

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import TextToolApp


class EncryptionView(tk.Toplevel):
    def __init__(self, root: "TextToolApp", decode: bool):
        super().__init__(root)
        self.root = root

        self.title("Шифратор")
        self.geometry("250x190")
        self.resizable(False, False)

        self.mode_var = tk.StringVar(value="Дешифровать" if decode else "Зашифровать")
        self.cipher_var = tk.StringVar(value="ROT13")

        tk.Label(self, text="Режим:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.OptionMenu(self, self.mode_var, "Зашифровать", "Дешифровать").grid(
            row=0, column=1, columnspan=2, sticky="we", padx=5, pady=5
        )

        tk.Label(self, text="Метод:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.OptionMenu(self, self.cipher_var, "ROT13", "Цезарь", "Атбаш", "Виженер", "XOR").grid(
            row=1, column=1, columnspan=2, sticky="we", padx=5, pady=5
        )

        self.options_frame = tk.Frame(self)
        self.options_frame.grid(row=2, column=0, columnspan=2, pady=5)

        self.complete_button = tk.Button(self, text="Выполнить")
        self.complete_button.grid(row=3, column=0, padx=5, pady=5, sticky="we")

        self.copy_button = tk.Button(self, text="Копировать")
        self.copy_button.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        self.columnconfigure(1, weight=1)

        self.params = {}
        self.param_configs = {
            "цезарь": [("Сдвиг:", "shift")],
            "xor": [("Ключ:", "xor_key")],
            "виженер": [("Ключ:", "vigenere_key")],
            "rot13": [],
            "атбаш": [],
        }

    def create_fields(self) -> None:
        """Создаёт entry-поля в зависимости от метода"""
        self._update_options_frame()

        for row, (label, name) in enumerate(self.param_configs.get(self.cipher_var.get().lower(), [])):
            tk.Label(self.options_frame, text=label).grid(row=row, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(self.options_frame)
            entry.grid(row=row, column=1, padx=5, pady=5, sticky="we")
            self.params[name] = entry

    def get_params(self) -> dict[str, str]:
        """Возвращает все введённые значения"""
        return {
            name: widget.get()
            for name, widget in self.params.items() if widget.winfo_exists()
        }

    def _update_options_frame(self) -> None:
        """Обновляет панель параметров для выбранного шифра"""
        self.options_frame.destroy()
        self.options_frame = tk.Frame(self)
        self.options_frame.grid(row=2, column=0, columnspan=2, pady=5)
        self.params.clear()
