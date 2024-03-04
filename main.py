import sys
from PyQt5 import QtWidgets
from windows.student import Student
from windows.task import Task
from windows.algorithm import Algorithm


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 1200, 800)
        self.setWindowTitle("Лабораторна робота №2 з АМО")

        self.side_menu = QtWidgets.QListWidget(self)
        self.side_menu.addItem("Студент")
        self.side_menu.addItem("Завдання")
        self.side_menu.addItem("Алгоритм")
        self.side_menu.setFixedWidth(150)
        self.side_menu.setStyleSheet("background-color: #f2f2f2; font-size: 20px; font-weight: bold;")
        self.side_menu.itemClicked.connect(self.open_window)

        self.main_area = QtWidgets.QStackedWidget(self)
        self.window1 = Student()  # Замінив window1 на пустий QWidget
        self.window2 = Task()  # Замінив window2 на пустий QWidget
        self.window3 = Algorithm()
        self.main_area.addWidget(self.window1)
        self.main_area.addWidget(self.window2)
        self.main_area.addWidget(self.window3)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.side_menu)
        layout.addWidget(self.main_area)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_window(self, item):
        if item.text() == "Студент":
            self.main_area.setCurrentIndex(0)
        elif item.text() == "Завдання":
            self.main_area.setCurrentIndex(1)
        elif item.text() == "Алгоритм":
            self.main_area.setCurrentIndex(2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
