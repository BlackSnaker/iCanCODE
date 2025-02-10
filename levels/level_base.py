# levels/level_base.py

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QTextEdit,
    QMessageBox
)
from PyQt6.QtCore import Qt

class LevelBase(QWidget):
    """
    Базовый класс для уровней.
    Содержит основные элементы UI и базовые методы.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Заголовок уровня
        self.level_title = QLabel("Название уровня")
        self.level_title.setStyleSheet("font-size: 18pt; font-weight: bold;")
        self.layout.addWidget(self.level_title)

        # Описание задания
        self.task_description = QLabel("Описание задания")
        self.task_description.setWordWrap(True)
        self.layout.addWidget(self.task_description)

        # Поле для ввода кода/решения
        self.code_input = QTextEdit()
        self.code_input.setPlaceholderText("Введите решение или код здесь...")
        self.layout.addWidget(self.code_input)

        # Кнопки
        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.hint_button = QPushButton("Подсказка")
        self.check_button = QPushButton("Проверить")
        self.next_button = QPushButton("Следующий уровень")

        self.button_layout.addWidget(self.hint_button)
        self.button_layout.addWidget(self.check_button)
        self.button_layout.addWidget(self.next_button)

        # Привязываем сигналы кнопок к методам
        self.hint_button.clicked.connect(self.show_hint)
        self.check_button.clicked.connect(self.check_solution)
        self.next_button.clicked.connect(self.go_next_level)

    def show_hint(self):
        """ Показать подсказку. Переопределите в дочернем классе, если нужно. """
        QMessageBox.information(
            self,
            "Подсказка",
            "Это пример базовой подсказки. Переопределите show_hint в дочерних классах."
        )

    def check_solution(self):
        """ Проверка решения. Переопределите в дочерних классах. """
        QMessageBox.information(
            self,
            "Проверка",
            "Метод check_solution не реализован. Переопределите в дочернем классе!"
        )

    def go_next_level(self):
        """
        Переход к следующему уровню:
        Обращаемся к главному окну (self.window()) и вызываем у него next_level().
        """
        main_window = self.window()
        if main_window and hasattr(main_window, 'next_level'):
            main_window.next_level()
