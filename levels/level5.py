# levels/level5.py

from PyQt6.QtWidgets import QMessageBox
from .level_base import LevelBase

class Level5(LevelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.level_title.setText("Уровень 5: Функции")
        self.task_description.setText(
            "Задача: Определите функцию greet(name), которая выводит 'Привет, <name>!'.\n\n"
            "Пример:\n"
            "def greet(name):\n"
            "    print('Привет, ' + name + '!')"
        )

    def check_solution(self):
        code = self.code_input.toPlainText().strip()
        # Наивная проверка: ищем "def greet(" и "print("Привет"
        # Можно добавить проверку на вызов функции, но пока ограничимся этим.
        if "def greet(" in code and "Привет" in code:
            QMessageBox.information(
                self,
                "Проверка",
                "Отлично! Вы прошли уровень 5."
            )
        else:
            QMessageBox.warning(
                self,
                "Проверка",
                "Кажется, вы не определили функцию greet(name) или не выводите 'Привет, ...'.\n"
                "Проверьте синтаксис и вывод."
            )

    def show_hint(self):
        QMessageBox.information(
            self,
            "Подсказка",
            "Используйте ключевое слово def для определения функции.\n"
            "Например:\n\n"
            "def greet(name):\n"
            "    print('Привет, ' + name + '!')"
        )
