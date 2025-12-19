import re
import html

import pyperclip


class TextModel:
    def __init__(self):
        self.text = ""

    def set_text(self, text: str) -> None:
        """Задает текст"""
        self.text = text

    def get_text(self) -> str:
        """Возвращает текст"""
        return self.text

    def get_stats(self) -> dict:
        """Возвращает статистику по тексту"""
        text = self.text
        return {
            "Общее количество символов": len(text),
            "Количество букв": sum(ch.isalpha() for ch in text),
            "Количество слов": len(re.findall(r"\b\w+\b", text, re.UNICODE)),
            "Количество предложений": len([ch for ch in re.split(r'[.!?]+(?:\s+|$)', text) if ch]),
            "Количество гласных": sum(ch.lower() in "аеёиоуыэюяaeiou" for ch in text),
            "Количество согласных": sum(ch.lower() in "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz" for ch in text),
        }

    def copy(self) -> None:
        """Копирует текст в буфер обмена"""
        try:
            pyperclip.copy(self.text)
        except pyperclip.PyperclipException:
            return

    def paste(self) -> None:
        """Вставляет текст из буфера обмена"""
        try:
            self.text = pyperclip.paste()
        except pyperclip.PyperclipException:
            self.text = self.text

    def to_uppercase(self) -> None:
        """Преобразует текст в верхний регистр"""
        self.text = self.text.upper()

    def to_lowercase(self) -> None:
        """Преобразует текст в нижний регистр"""
        self.text = self.text.lower()

    def remove_empty_lines(self) -> None:
        """Удаляет пустые строки"""
        self.text = re.sub(r"\n\s*\n", "\n", self.text).strip()

    def remove_extra_spaces(self) -> None:
        """Удаляет лишние пробелы и форматирует текст"""
        self.text = re.sub(r"[ \t\r\f\v]+", " ", self.text)
        self.text = re.sub(r"\s+([,.!?;:])", r"\1", self.text)
        self.text = "\n".join(line.strip() for line in self.text.splitlines())

    def clean_html(self) -> None:
        """Удаляет HTML-теги"""
        self.text = html.unescape(re.sub("<[^<]+?>", "", self.text))

    def only_cyrillic(self) -> None:
        """Оставляет только кириллицу"""
        self.text = re.sub(r"[^А-Яа-яЁё]", " ", self.text)

    def only_latin(self) -> None:
        """Оставляет только латиницу"""
        self.text = re.sub(r"[^A-Za-z]", " ", self.text)

    def find_positions(self, query: str, match_case: bool, use_regex: bool) -> list[tuple[str, str]]:
        """Возвращает позиции совпадений для подсветки"""
        matches = []
        flag = 0 if match_case else re.IGNORECASE

        pattern_str = query if use_regex else re.escape(query)
        pattern = re.compile(pattern_str, flags=flag)

        for m in pattern.finditer(self.text):
            start = f"1.0+{m.start()}c"
            end = f"1.0+{m.end()}c"
            matches.append((start, end))

        return matches

    def replace_text(self, search: str, replace: str, match_case: bool, use_regex: bool) -> str:
        """Заменяет найденный текст"""
        flag = 0 if match_case else re.IGNORECASE

        pattern = search if use_regex else re.escape(search)
        return re.sub(pattern, replace, self.text, flags=flag)
