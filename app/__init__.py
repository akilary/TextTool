from .gui import MainApp


def create_app() -> MainApp:
    """Создание приложение"""
    app = MainApp()
    return app
