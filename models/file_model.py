from tkinter import filedialog


class FileModel:
    def __init__(self):
        self.text = ""

    def set_text(self, text: str) -> None:
        """Задает текст"""
        self.text = text

    def get_text(self) -> str:
        """Возвращает текст"""
        return self.text

    def open_file(self) -> None:
        """Открывает файлы формата .txt и .html"""
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("HTML Files", "*.html")])
        if not filepath: return

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                self.text = file.read()
        except OSError:
            self.text = ""

    def save_file(self) -> None:
        """Сохраняет файл в формате .txt"""
        filepath = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")], initialfile="my_file.txt")
        if filepath != "":
            text = self.text
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(text)

    def save_as(self) -> None:
        """Сохраняет в произвольном формате"""
        filepath = filedialog.asksaveasfilename(filetypes=[("All Files", "*.*")], initialfile="my_file")
        if filepath != "":
            text = self.text
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(text)
