from typing import Callable

from models import EncryptionModel, TextModel
from utils import require_view
from views import MainView, EncryptionView


class EncryptionController:
    def __init__(self, main_view: MainView, encryption_model: EncryptionModel, text_model: TextModel):
        self.main_view = main_view
        self.encryption_model = encryption_model
        self.text_model = text_model
        self.encryption_view: EncryptionView | None = None

    def _open_view(self, decode: bool) -> None:
        """Открывает окно шифрования"""
        if self.encryption_view and self.encryption_view.winfo_exists():
            self.encryption_view.lift()
            return

        self.encryption_view = EncryptionView(self.main_view.root, decode)
        self.encryption_view.cipher_var.trace_add("write", self._update_fields)

        self.encryption_view.complete_button.config(command=self._complete)
        self.encryption_view.copy_button.config(command=self._copy)
        self.encryption_view.protocol("WM_DELETE_WINDOW", self._close)

    @require_view("encryption_view")
    def _update_fields(self, *_) -> None:
        """Обновляет текстовые поля"""
        self.encryption_view.create_fields()

    @require_view("encryption_view")
    def _complete(self) -> None:
        """Выполняет выбранное шифрование"""
        self.encryption_model.set_text(self.main_view.editor.get("1.0", "end-1c"))

        decode = self.encryption_view.mode_var.get().lower() == "дешифровать"
        params = self.encryption_view.get_params()

        ciphers = {
            "цезарь": lambda: self._process_caesar(decode, params.get("shift", "")),
            "rot13": lambda: self._process_rot13(),
            "атбаш": lambda: self._process_atbash(),
            "виженер": lambda: self._process_vigenere(decode, params.get("vigenere_key", "")),
            "xor": lambda: self._process_xor(params.get("xor_key", "")),
        }
        cipher_name = self.encryption_view.cipher_var.get().lower()
        action = ciphers.get(cipher_name)

        if action and cipher_name in ("цезарь", "виженер", "xor") and not list(params.values())[0]: return

        action()

        self.main_view.editor.delete("1.0", "end-1c")
        self.main_view.editor.insert("1.0", self.encryption_model.get_text(), "end-1c")

    @require_view("encryption_view")
    def _copy(self) -> None:
        """Копирует результат"""
        self.text_model.set_text(self.encryption_model.get_text())
        self.text_model.copy()

    @require_view("encryption_view")
    def _process_caesar(self, decode: bool, shift: str) -> None:
        """Шифр Цезаря"""
        if shift.isdigit():
            self.encryption_model.caesar(decode, int(shift))

    @require_view("encryption_view")
    def _process_rot13(self) -> None:
        """Шифр ROT13"""
        self.encryption_model.rot13()

    @require_view("encryption_view")
    def _process_atbash(self) -> None:
        """Шифр Атбаш"""
        self.encryption_model.atbash()

    @require_view("encryption_view")
    def _process_vigenere(self, decode: bool, vigenere_key: str) -> None:
        """Шифр Виженера"""
        self.encryption_model.vigenere(decode, vigenere_key)

    @require_view("encryption_view")
    def _process_xor(self, key: str) -> None:
        """Шифр XOR"""
        self.encryption_model.xor(key)

    def _close(self) -> None:
        """Закрывает окно"""
        if self.encryption_view:
            self.encryption_view.destroy()
            self.encryption_view = None

    def get_actions(self) -> dict[str, Callable[[], None]]:
        """Возвращает доступные действия"""
        return {
            "Зашифровать": lambda: self._open_view(False),
            "Дешифровать": lambda: self._open_view(True),
        }
