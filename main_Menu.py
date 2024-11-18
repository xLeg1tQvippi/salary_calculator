from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
import sys
import dataText


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.objects()
        self.layouts()
        self.layout_connection()
        self.apply_styles()

    def init_ui(self):
        # Обрисовка программы.
        self.setWindowTitle(dataText.menu_title)
        self.resize(dataText.win_sizes["width"], dataText.win_sizes["height"])
        self.setWindowOpacity(1)

    def apply_styles(self):
        # Изменение стилей под кнопки и UI
        self.setStyleSheet(
            """
            QWidget {
                font-size: 16px;
            }
            QPushButton {
                background-color: #BCBCBC;      /* Светло-серый фон */
                color: #333;                    /* Темный текст */
                font-size: 17px;                /* Средний размер шрифта */
                border: 2px solid #BCBCBC;         /* Легкая серая рамка */
                padding: 5px 10px;              /* Отступы внутри кнопки */
                text-align: center;             /* Выравнивание текста по центру */
                outline: none;                  /* Убираем обводку при фокусе */
            }

            QPushButton:hover {
                background-color: #e0e0e0;      /* Более темный серый фон при наведении */
            }

            QPushButton:pressed {
                background-color: #d0d0d0;      /* Еще более темный фон при нажатии */
            }

            QPushButton:disabled {
                background-color: #f7f7f7;      /* Очень светлый фон для неактивных кнопок */
                color: #aaa;                    /* Светло-серый текст для неактивных кнопок */
                border: 1px solid #ddd;         /* Серая рамка для неактивных кнопок */
            }
            """
        )

    def objects(self):
        # Создание кнопок, виджетов и др.
        self.welcomeText = QLabel(dataText.menu_welcome_text)
        self.button_history = QPushButton(dataText.menu_history)
        self.button_append = QPushButton(dataText.menu_append)
        self.button_check_info = QPushButton(dataText.menu_list)

    def layouts(self):
        # Линии по которым будут лежать кнопки и др.
        self.vlayout = QVBoxLayout()
        self.hlayout = QHBoxLayout()

    def layout_connection(self):
        # Подключение объектов к линиям.
        self.vlayout.addWidget(self.welcomeText)
        self.hlayout.addWidget(self.button_history)
        self.hlayout.addWidget(self.button_append)
        self.hlayout.addWidget(self.button_check_info)

        self.vlayout.addLayout(self.hlayout)
        self.setLayout(self.vlayout)

    def connections(self):
        # Коннект кнопок и др.
        pass


if __name__ == "__main__":
    print("Initializing Menu ...")
    app = QApplication([])

    win = Menu()
    win.show()

    sys.exit(app.exec())
