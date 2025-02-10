# levels/level6.py

from PyQt6.QtWidgets import (
    QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsRectItem
)
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QBrush, QColor
from .level_base import LevelBase

class Level6(LevelBase):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.level_title.setText("Уровень 6: Дойти из точки A в точку B!")
        self.task_description.setText(
            "Задача: Напишите код, который «двинет» персонажа от x=0 до x=200.\n"
            "Подсказка: используйте цикл for, где в каждой итерации «вызываете» move_right().\n"
            "Это упрощённый пример: мы просто проверяем, есть ли в коде for и move_right()."
        )

        # Создаем сцену и виджет QGraphicsView
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setFixedHeight(300)  # ограничим высоту, чтобы уместилось в интерфейс

        # Вставляем QGraphicsView в общий layout - перед полем ввода кода или после описания
        # Например, вставим сразу после описания задания:
        self.layout.insertWidget(2, self.view)

        # Создаем "персонажа" — прямоугольник 30x30
        self.player = QGraphicsRectItem(0, 0, 30, 30)
        self.player.setBrush(QBrush(QColor("blue")))
        self.scene.addItem(self.player)

        # Создаем "точку B" — прямоугольник 30x30, расположенный на x=200
        self.goal = QGraphicsRectItem(200, 0, 30, 30)
        self.goal.setBrush(QBrush(QColor("green")))
        self.scene.addItem(self.goal)

        # Устанавливаем границы сцены (чтобы было видно фон, если захотите)
        self.scene.setSceneRect(0, 0, 400, 300)

        # Можно установить цвет фона
        self.scene.setBackgroundBrush(QColor("#e0e0e0"))

        # Дополнительные поля для анимации
        self.timer = None
        self.current_step = 0
        self.max_steps = 0
        self.step_distance = 0

    def check_solution(self):
        """
        Простейшая проверка: ищем в тексте 'for' и 'move_right()'.
        Если находим, считаем, что нужно запустить анимацию.
        """
        code = self.code_input.toPlainText().strip().lower()
        if "for" in code and "move_right()" in code:
            self.animate_player_to_goal()
        else:
            QMessageBox.warning(
                self,
                "Проверка",
                "Кажется, вы не используете цикл for и move_right().\n"
                "Попробуйте ещё раз!"
            )

    def show_hint(self):
        """
        Подсказка, как можно «притвориться», что мы вызываем move_right()
        несколько раз. 
        """
        QMessageBox.information(
            self,
            "Подсказка",
            "Используйте что-то вроде:\n\n"
            "for i in range(5):\n"
            "    move_right()\n\n"
            "Допустим, move_right() сдвигает игрока на 40 пикселей вправо, 5 раз."
        )

    def animate_player_to_goal(self):
        """
        Запускаем анимацию, имитирующую 5 (или иное число) шагов вправо.
        Вы можете усложнить логику и реально парсить кол-во шагов из кода.
        """
        self.current_step = 0
        self.max_steps = 5        # сделаем 5 шагов
        self.step_distance = 40   # каждый шаг - 40 пикселей

        # Сбрасываем позицию игрока (на случай повторных проверок)
        self.player.setX(0)

        # Создаём QTimer, чтобы поэтапно двигать персонажа
        self.timer = QTimer()
        self.timer.timeout.connect(self.do_step)
        self.timer.start(300)  # 300 мс между шагами

    def do_step(self):
        if self.current_step < self.max_steps:
            # Двигаем игрока вправо на step_distance
            self.player.moveBy(self.step_distance, 0)
            self.current_step += 1
        else:
            # Анимация завершена
            self.timer.stop()

            # Проверяем, достигли ли мы цели
            player_x = self.player.x()
            goal_x = self.goal.x()

            # Если персонаж в точке (200, 0) (или очень близко)
            if abs(player_x - goal_x) < 1:
                QMessageBox.information(
                    self,
                    "Проверка",
                    "Отлично! Вы прошли уровень 6."
                )
            else:
                QMessageBox.warning(
                    self,
                    "Проверка",
                    "Персонаж не дошёл до точки B. Возможно, нужно больше шагов?"
                )
