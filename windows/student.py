from PyQt5 import QtWidgets, QtGui, QtCore

class Student(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


        # Додавання вмісту віджету
        label = QtWidgets.QLabel("Інформація про студента:\n\nГрупа: ІО-24\nІм'я: Федонюк Роман\nЗалікова: 2429\nВаріант: 29\n")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("font-size: 34px; font-weight: bold;")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

