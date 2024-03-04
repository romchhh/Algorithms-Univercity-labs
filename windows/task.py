from PyQt5 import QtWidgets, QtGui, QtCore

class Task(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Завантаження зображення
        image_label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("content/task.png")
        pixmap = pixmap.scaled(950, 700, QtCore.Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(QtCore.Qt.AlignCenter)

        # Розміщення віджетів у макеті
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(image_label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
