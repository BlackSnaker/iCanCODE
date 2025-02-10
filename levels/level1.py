# levels/level1.py

from PyQt6.QtWidgets import QMessageBox
from .level_base import LevelBase

class Level1(LevelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.level_title.setText("Уровень 1: Простой вывод")
        self.task_description.setText(
            "Задача: Напишите программу, которая выводит строку: 'Привет, мир!'.\n"
            "Подсказка: Используйте функцию print."
        )

    def check_solution(self):
        code = self.code_input.toPlainText().strip()
        # Простейшая проверка: проверяем, что в коде есть print("Привет, мир!")
        if 'print("Привет, мир!")' in code or "print('Привет, мир!')" in code:
            QMessageBox.information(
                self,
                "Проверка",
                "Отлично! Вы прошли уровень 1."
            )
        else:
            QMessageBox.warning(
                self,
                "Проверка",
                "Похоже, что ваш код не содержит нужную строку.\nПопробуйте ещё раз!"
            )

    def show_hint(self):
        """ Дополнительная подсказка именно для этого уровня. """
        QMessageBox.information(
            self,
            "Подсказка",
            "Используйте функцию print. Например:\nprint('Привет, мир!')"
        )
