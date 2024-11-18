from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
)
from PyQt6.QtCore import Qt
import sys
import dataText


class Append_Info(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.objects()
        self.layouts()
        self.layouts_connect()

    def init_ui(self):
        self.setWindowTitle(dataText.append_title)
        self.resize(dataText.append_sizes["width"], dataText.append_sizes["height"])

    def objects(self):
        self.salary = QLineEdit()
        self.salary_text = QLabel(dataText.salary_text)
        self.goal = QLineEdit()
        self.goal_text = QLabel(dataText.goal_text)
        self.begining_date = QLineEdit()  # Изменить под дату.
        self.begining_date_text = QLabel(dataText.begining_date_text)
        self.finishing_date = QLineEdit()  # Изменить под дату.
        self.finishing_date_text = QLabel(dataText.finishing_date_text)
        # self.currency - Выпадающий список
        # self.transfer_currency - валюта в которую делается перевод.
        self.button = QPushButton(dataText.button_text)
        self.objects_data()
        self.objects_connection()

    def objects_data(self):
        self.salary.setFixedWidth(200)
        self.goal.setFixedWidth(200)
        self.begining_date.setFixedWidth(200)
        self.finishing_date.setFixedWidth(200)
        self.button.setFixedWidth(200)

        # Текст подсказки для QLineEdit:

        self.salary.setPlaceholderText("20_000")
        self.goal.setPlaceholderText("100_000")
        self.begining_date.setPlaceholderText("18/11/2024")
        self.finishing_date.setPlaceholderText("05/02/2025")

    def objects_connection(self):
        # self.button.clicked.connect()
        pass

    def layouts(self):
        self.hlayout = QHBoxLayout()
        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.vlayout = QVBoxLayout()
        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()

    def layouts_connect(self):
        self.vlayout.addWidget(self.salary_text)
        self.vlayout.addWidget(self.salary)
        self.vlayout.addWidget(self.goal_text)
        self.vlayout.addWidget(self.goal)
        self.vlayout.addWidget(self.begining_date_text)
        self.vlayout.addWidget(self.begining_date)
        self.vlayout.addWidget(self.finishing_date_text)
        self.vlayout.addWidget(self.finishing_date)
        self.vlayout.addWidget(self.button)

        self.hlayout.addLayout(self.vlayout)
        self.hlayout.setAlignment(self.vlayout, Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.hlayout)


if __name__ == "__main__":
    app = QApplication([])

    win = Append_Info()
    win.show()

    sys.exit(app.exec())
