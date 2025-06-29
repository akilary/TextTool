import inspect
from typing import Callable

from . import commands

class Cfg:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    MODAL_WIDTH = 360
    MODAL_HEIGHT = 200

    FONT_NAME = "Arial"

    MENU_CONFIG = {
        "Файл": [
            {"label": "Открыть TXT/HTML", "command": "open_file"},
            {"label": "Сохранить TXT", "command": "save_file"},
            {"label": "Сохранить как...", "command": "save_as"},
            {"label": "Выход", "command": "close_app"},
        ],
        "Правка": [
            {"label": "Копировать", "command": "copy_text"},
            {"label": "Вставить", "command": "paste_text"},
            {"label": "Отмена", "command": "undo_text"},
        ],
        "Обработка текста": [
            {"label": "Верхний регистр", "command": "to_uppercase"},
            {"label": "Нижний регистр", "command": "to_lowercase"},
            {"label": "Удалить пустые строки", "command": "remove_empty_lines"},
            {"label": "Удалить лишние пробелы", "command": "remove_extra_spaces"},
            {"label": "Очистить HTML", "command": "clean_html"},
            {"label": "Регулярные выражения (открывает отдельное окно)", "command": "regex"},
        ],
        "Анализ": [
            {"label": "Проверка орфографии", "command": None}
        ],
        "Шифрование": [
            {"label": "Зашифровать", "command": None},
            {"label": "Дешифровать", "command": None}
        ],
        "Фильтры": [
            {"label": "Оставить только кириллицу", "command": None},
            {"label": "Оставить только латиницу", "command": None},
        ]
    }

    def get_command_registry(self) -> dict[str, Callable]:
        """Возвращает словарь доступных команд из конфигурации меню """
        available_funcs = {
            name: func
            for name, func in inspect.getmembers(commands, inspect.isfunction)
        }

        registry = {}
        for items in self.MENU_CONFIG.values():
            for item in items:
                cmd = item.get("command")
                if cmd and cmd in available_funcs:
                    registry[cmd] = available_funcs[cmd]
        return registry
