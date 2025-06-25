from nltk import download
from nltk.data import find

from .gui import TextTool


def create_app() -> TextTool:
    """Создание приложение"""
    app = TextTool()

    for resource in ["punkt", "punkt_tab"]:
        try:
            find(f"tokenizers/{resource}")
        except LookupError:
            download(resource)

    return app
