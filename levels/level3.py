# levels/level3.py

from PyQt6.QtWidgets import QMessageBox
from .level_base import LevelBase

class Level3(LevelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.level_title.setText("Уровень 3: Списки")
        self.task_description.setText(
            "Задача: Создайте список из нескольких элементов (например, чисел),\n"
            "затем выведите его длину с помощью функции len.\n\n"
            "Подсказка:\n"
            "my_list = [1, 2, 3]\n"
            "print(len(my_list))"
        )

    def check_solution(self):
        code = self.code_input.toPlainText().strip()
        # Пример наивной проверки: ищем "=[" и "len(" и "print("
        if "[" in code and "len(" in code and "print(" in code:
            QMessageBox.information(
                self,
                "Проверка",
                "Отлично! Вы прошли уровень 3."
            )
        else:
            QMessageBox.warning(
                self,
                "Проверка",
                "Кажется, вы не создали список или не вывели его длину.\n"
                "Проверьте, что используете len(имя_списка) и print(...)."
            )

    def show_hint(self):
        QMessageBox.information(
            self,
            "Подсказка",
            "Списки создаются в квадратных скобках.\nНапример: my_list = [10, 20, 30]\n"
            "Функция len(...) возвращает длину списка."
        )
