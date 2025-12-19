class EncryptionModel:
    RU_ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    EN_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    ALPHABETS = [
        (RU_ALPHABET, RU_ALPHABET.upper()),
        (EN_ALPHABET, EN_ALPHABET.upper()),
    ]

    def __init__(self):
        self.text = ""

    def set_text(self, text: str) -> None:
        """Задает текст"""
        self.text = text

    def get_text(self) -> str:
        """Возвращает текст"""
        return self.text

    def caesar(self, decode: bool, shift: int) -> None:
        """Шифр Цезаря - логика"""
        self.text = "".join(self._shift_char(ch, decode, shift) for ch in self.text)

    def rot13(self) -> None:
        """Шифр ROT13 (только для латиницы) - логика"""
        self.text = "".join(
            self._shift_char(ch, False, 13) if self._is_latin(ch) else ch
            for ch in self.text
        )

    def atbash(self) -> None:
        """Шифр Атбаш - логика"""
        self.text = "".join(
            self._shift_char(ch, False, atbash=True) if ch else ch
            for ch in self.text
        )

    def vigenere(self, decode: bool, key: str) -> None:
        """Шифр Виженера - логика"""
        res = []
        key_i = 0

        for ch in self.text:
            for lower, upper in self.ALPHABETS:
                if ch in lower or ch in upper:
                    key_ch = key[key_i % len(key)]
                    if key_ch in lower:
                        shift = lower.index(key_ch)
                    elif key_ch in upper:
                        shift = upper.index(key_ch)
                    else:
                        res.append(ch)
                        break

                    res.append(self._shift_char(ch, decode, shift))
                    key_i += 1
                    break
            else:
                res.append(ch)

        self.text = "".join(res)

    def xor(self, key: str) -> None:
        """Шифр XOR - логика"""
        encrypted = [
            ord(c) ^ ord(key[i % len(key)])
            for i, c in enumerate(self.text)
        ]
        self.text = "".join(chr(num) for num in encrypted)

    def _shift_char(self, ch: str, decode: bool, shift: int = 0, atbash: bool = False) -> str:
        """Сдвиг символа на N символов"""
        shift = -shift if decode else shift
        for lower, upper in self.ALPHABETS:
            if ch in lower:
                i = (lower.index(ch) + shift) % len(lower) if not atbash else len(lower) - 1 - lower.index(ch)
                return lower[i]
            elif ch in upper:
                i = (upper.index(ch) + shift) % len(upper) if not atbash else len(upper) - 1 - upper.index(ch)
                return upper[i]
        return ch

    def _is_latin(self, ch: str) -> bool:
        """Проверяет, является ли символ латинским"""
        return ch in self.EN_ALPHABET or ch in self.EN_ALPHABET.upper()
