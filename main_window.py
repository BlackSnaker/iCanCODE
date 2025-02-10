# main_window.py

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QStackedWidget,
    QMenuBar,
    QMenu,
    QMessageBox
)
from PyQt6.QtGui import QAction

# Импортируем уровни
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3 import Level3
from levels.level4 import Level4
from levels.level5 import Level5
from levels.level6 import Level6  # <-- наш новый "графический" уровень

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Игра: Учим Python через квесты")

        # Центральный виджет и лейаут
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        central_widget.setLayout(self.layout)

        # StackedWidget для переключения между уровнями
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Список уровней
        self.levels = []
        self.current_level_index = 0

        # Инициализируем уровни
        self.levels.append(Level1(parent=self.stacked_widget))  # Уровень 1
        self.levels.append(Level2(parent=self.stacked_widget))  # Уровень 2
        self.levels.append(Level3(parent=self.stacked_widget))  # Уровень 3
        self.levels.append(Level4(parent=self.stacked_widget))  # Уровень 4
        self.levels.append(Level5(parent=self.stacked_widget))  # Уровень 5
        self.levels.append(Level6(parent=self.stacked_widget))  # Уровень 6 (новый)

        # Добавляем уровни в QStackedWidget
        for level in self.levels:
            self.stacked_widget.addWidget(level)

        # Устанавливаем первый уровень
        self.stacked_widget.setCurrentIndex(self.current_level_index)

        # Создаём меню
        self.create_menus()

    def create_menus(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # Меню "Уровень"
        level_menu = QMenu("Уровень", self)
        menu_bar.addMenu(level_menu)

        # Пункт меню "Информация об уровне"
        info_action = QAction("Информация об уровне", self)
        info_action.triggered.connect(self.show_level_info)
        level_menu.addAction(info_action)

        # Пункт меню "Перезапустить уровень"
        restart_action = QAction("Перезапустить уровень", self)
        restart_action.triggered.connect(self.restart_current_level)
        level_menu.addAction(restart_action)

    def show_level_info(self):
        """Показывает информацию о текущем уровне."""
        level_number = self.current_level_index + 1
        QMessageBox.information(
            self,
            f"Информация об уровне {level_number}",
            f"Вы на уровне {level_number}.\n"
            "Выполните задание, нажмите 'Проверить', затем 'Следующий уровень'."
        )

    def restart_current_level(self):
        """Перезапуск (сброс) текущего уровня."""
        current_level_widget = self.levels[self.current_level_index]
        current_level_widget.code_input.clear()

    def next_level(self):
        """Переходит к следующему уровню."""
        if self.current_level_index < len(self.levels) - 1:
            self.current_level_index += 1
            self.stacked_widget.setCurrentIndex(self.current_level_index)
        else:
            QMessageBox.information(
                self,
                "Поздравляем!",
                "Вы прошли все доступные уровни!"
            )
