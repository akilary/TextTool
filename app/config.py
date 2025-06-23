from .commands import *


class Cfg:
    menu_config = {
        "Файл": [
            {"label": "Открыть TXT/HTML", "command": "open_file"},
            {"label": "Сохранить TXT", "command": "save_file"},
            {"label": "Сохранить как...", "command": "save_as"},
            {"label": "Выход", "command": "close_app"},
        ],
        "Правка": [
            {"label": "Копировать", "command": "copy_text"},
            {"label": "Вставить", "command": "insert_text"},
            {"label": "Отмена", "command": "undo_text"},
        ],
        "Обработка текста": [
            {"label": "Удалить пустые строки", "command": "remove_empty_lines"},
            {"label": "Удалить лишние пробелы", "command": "remove_extra_spaces"},
            # {"label": "Начать с заглавной буквы", "command": None},
            # {"label": "Верхний регистр", "command": None},
            # {"label": "Нижний регистр", "command": None},
            # {"label": "Очистить HTML", "command": None},
            # {"label": "Регулярные выражения (открывает отдельное окно)", "command": None},
        ],
        # "Анализ": [
        #     {"label": "Проверка орфографии", "command": None}
        # ],
        # "Шифрование": [
        #     {"label": "Зашифровать", "command": None},
        #     {"label": "Дешифровать", "command": None}
        # ],
        # "Фильтры": [
        #     {"label": "Оставить только кириллицу", "command": None},
        #     {"label": "Оставить только латиницу", "command": None},
        # ]
    }

    command_registry = {
        "open_file": open_file,
        "save_file": save_file,
        "save_as": save_as,
        "close_app": close_app,
        "copy_text": copy_text,
        "insert_text": insert_text,
        "undo_text": undo_text,
        "remove_empty_lines": remove_empty_lines,
        "remove_extra_spaces": remove_extra_spaces,
    }
