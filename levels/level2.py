# levels/level2.py

from PyQt6.QtWidgets import QMessageBox
from .level_base import LevelBase

class Level2(LevelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.level_title.setText("Уровень 2: Работа с переменными")
        self.task_description.setText(
            "Задача: Создайте переменную x = 5, затем выведите её значение.\n"
            "Подсказка: используйте конструкции:\n\n"
            "x = 5\n"
            "print(x)"
        )

    def check_solution(self):
        code = self.code_input.toPlainText().strip()
        # Наивная проверка
        if "x = 5" in code and "print(x)" in code:
            QMessageBox.information(
                self,
                "Проверка",
                "Отлично! Вы прошли уровень 2."
            )
        else:
            QMessageBox.warning(
                self,
                "Проверка",
                "Похоже, что ваш код не решает задачу.\n"
                "Убедитесь, что вы создали переменную x=5 и вывели её."
            )

    def show_hint(self):
        QMessageBox.information(
            self,
            "Подсказка",
            "Чтобы присвоить переменной значение, используйте =.\n"
            "Например, x = 5.\n"
            "Чтобы вывести значение, используйте print(x)."
        )
