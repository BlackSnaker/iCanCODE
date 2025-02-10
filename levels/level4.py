# levels/level4.py

from PyQt6.QtWidgets import QMessageBox
from .level_base import LevelBase


class Level4(LevelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.level_title.setText("Уровень 4: Циклы")
        self.task_description.setText(
            "Задача: Используйте цикл for, чтобы вывести числа от 1 до 5.\n\n"
            "Подсказка:\n"
            "for i in range(1, 6):\n"
            "    print(i)"
        )

    def check_solution(self):
        code = self.code_input.toPlainText().strip()
        # Наивная проверка: ищем "for", "in range" и "print("
        if "for " in code and "range(" in code and "print(" in code:
            QMessageBox.information(
                self,
                "Проверка",
                "Отлично! Вы прошли уровень 4."
            )
        else:
            QMessageBox.warning(
                self,
                "Проверка",
                "Кажется, вы не используете цикл for с range(1,6) или не выводите значения.\n"
                "Проверьте синтаксис."
            )

    def show_hint(self):
        QMessageBox.information(
            self,
            "Подсказка",
            "С помощью range(1, 6) вы получите числа от 1 до 5.\n"
            "Перебирайте их циклом for и выводите каждое число."
        )
