"""Python RPG — уровень 1, «Потерянный реестр».

Стартовая заготовка (НЕ готовое решение).
Твои задачи: дописать функции add_quest, show_quests и complete_quest.

Как запустить:
    py registry.py       # Windows, если установлен Python Launcher
    python registry.py   # другой вариант

Автоматическая печать Гильдии рассчитана на интерфейс функций:
    add_quest(quests), show_quests(quests), complete_quest(quests), main()
и список словарей вида {"title": "...", "done": False}.
Можно менять внутренние алгоритмы и добавлять функции, но для
автономной самопроверки оставь эти названия, сигнатуры и меню 1–4.

Код сохраняй в ЭТОТ файл, рядом с self_check.py. Нажми Ctrl+S.
"""


def add_quest(quests):
    """Попросить название и добавить новое поручение в список."""
    title = input("Название поручения: ").strip()
    if not title:
        print("Название не может быть пустым.")
        return
    quests.append({"title": title, "done": False})
    print(f"Поручение «{title}» добавлено.")


def show_quests(quests):
    """Показать все поручения с номерами и статусами."""
    if not quests:
        print("Поручений пока нет.")
        return
    for number, quest in enumerate(quests, start=1):
        mark = "[x] выполнено" if quest["done"] else "[ ] не выполнено"
        print(f"{number}. {quest['title']} — {mark}")


def complete_quest(quests):
    """Отметить выбранное по номеру поручение выполненным."""
    if not quests:
        print("Поручений пока нет.")
        return
    raw = input(f"Номер поручения (1–{len(quests)}): ").strip()
    try:
        number = int(raw)
    except ValueError:
        print("Нужно ввести число, например 1.")
        return
    if not 1 <= number <= len(quests):
        print(f"Нет поручения с номером {number}. Выбери от 1 до {len(quests)}.")
        return
    quests[number - 1]["done"] = True
    print(f"Поручение «{quests[number - 1]['title']}» выполнено.")


def main():
    quests = []
    while True:
        print("\n=== РЕЕСТР АУРИОНА ===")
        print("1 — Добавить поручение")
        print("2 — Показать поручения")
        print("3 — Отметить выполненным")
        print("4 — Выход")
        choice = input("Команда: ").strip()

        if choice == "1":
            add_quest(quests)
        elif choice == "2":
            show_quests(quests)
        elif choice == "3":
            complete_quest(quests)
        elif choice == "4":
            print("Записи закрыты. До встречи в Гильдии!")
            break
        else:
            print("Неизвестная команда. Выбери число от 1 до 4.")


if __name__ == "__main__":
    main()
