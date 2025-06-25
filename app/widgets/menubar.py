import tkinter as tk


def create_menubar(r) -> None:
    """Создаёт меню-бар"""
    cfg = r.cfg
    menu_cfg = cfg.MENU_CONFIG
    commands_registry = cfg.get_command_registry()

    main_menu = tk.Menu(r)

    for menu_name, items in menu_cfg.items():
        menu = tk.Menu(main_menu, tearoff=False)

        for item in items:
            command_name = item["command"]
            label = item["label"]

            if command_name in commands_registry:
                func = commands_registry[command_name]
                menu.add_command(label=label, command=lambda f=func: f(r))
            else:
                menu.add_command(label=label, command=lambda: print("Функция не найдена"))

        main_menu.add_cascade(label=menu_name, menu=menu)

    r.config(menu=main_menu)
