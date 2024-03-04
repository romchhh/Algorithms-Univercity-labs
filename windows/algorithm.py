import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import matplotlib.pyplot as plt
import numpy as np

import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import matplotlib.pyplot as plt
import numpy as np

class ArrayInput(QtWidgets.QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Введіть масив")
        self.setMinimumWidth(200)
        self.setMinimumHeight(60)
        font = self.font()
        font.setPointSize(14)
        self.setFont(font)

class ArrayOutput(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setMinimumHeight(40)
        font = self.font()
        font.setPointSize(14)
        self.setFont(font)

class FileDropField(QtWidgets.QTextEdit):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setMinimumHeight(100)
        self.setPlaceholderText("\n                                      📂Оберіть або перетягніть файл.")
        font = self.font()
        font.setPointSize(14)
        self.setFont(font)

class SortingButton(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__("Сортувати")
        self.setStyleSheet("background-color: green; color: white; border: 1px solid black; padding: 10px;")  

class Algorithm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.text_fields = [ArrayInput() for _ in range(10)]
        self.output_fields = [ArrayOutput() for _ in range(10)]
        self.drop_field = FileDropField()
        self.button = SortingButton()

        layout = QtWidgets.QVBoxLayout()
        for text_field, output_field in zip(self.text_fields, self.output_fields):
            h_layout = QtWidgets.QHBoxLayout()
            h_layout.addWidget(text_field)
            h_layout.addWidget(output_field)
            layout.addLayout(h_layout)

        layout.addWidget(self.drop_field)
        layout.addWidget(self.button)
        layout.setSpacing(10)

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QtWidgets.QWidget()
        scroll_widget.setLayout(layout)
        scroll_area.setWidget(scroll_widget)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        self.drop_field.dragEnterEvent = self.drag_enter_event
        self.drop_field.dropEvent = self.drop_event
        self.drop_field.mousePressEvent = self.choose_file

        self.button.clicked.connect(self.sort_arrays)
        
    def choose_file(self, event):
        # Відкриття діалогового вікна для вибору файлу
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'Text files (*.txt)')
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    arrays = []
                    for line in file:
                        if line.strip().startswith('[') and line.strip().endswith(']'):
                            line = line.strip()[1:-1]  # Видаляємо квадратні дужки з початку та кінця рядка
                            numbers = []
                            for val in line.split():
                                try:
                                    num = float(val)
                                    numbers.append(num)
                                except ValueError:
                                    # Якщо значення не може бути конвертоване у float, вивести повідомлення
                                    self.output_fields[0].setPlainText("❗Не числове значення.")
                                    break
                            else:
                                # Якщо всі значення конвертовані у float, додати масив у список для сортування
                                arrays.append(numbers)
                                continue
                        # Очистити вихідне поле, якщо значення недійсне
                            self.output_fields[0].clear()

                        # Вивести повідомлення про помилку поруч з відповідним текстовим полем
                            self.output_fields[0].setPlainText("❗Не числове значення.")

                    # Вивід масивів у відповідні текстові поля
                    for i, array in enumerate(arrays):
                        if i < len(self.text_fields):
                            # Роздвляємо масив квадратними дужками [] і розділяємо елементи пробілами
                            formatted_array = "[" + " ".join(map(str, array)) + "]"
                            self.text_fields[i].setText(formatted_array)
            except Exception as e:
                print("Error:", e)

    def sort_arrays(self):
    # Отримання масивів з текстових полів
        arrays = []
        times = []  # Зберігаємо часи сортування для побудови графіка
        for i, text_field in enumerate(self.text_fields):
            text = text_field.text().strip()  # Видаляємо зайві пробіли з початку і кінця рядка
            if text.startswith('[') and text.endswith(']'):
                text = text[1:-1]  # Видаляємо квадратні дужки з початку та кінця масиву
                numbers = []
                for val in text.split():
                    try:
                        num = float(val)
                        numbers.append(num)
                    except ValueError:
                        # Якщо значення не може бути конвертоване у float, вивести повідомлення
                        self.output_fields[i].setPlainText("❗Не числове значення.")
                        break
                else:
                    # Якщо всі значення конвертовані у float, додати масив у список для сортування
                    arrays.append(numbers)
                    self.output_fields[i].setPlainText("")  # Очищаємо вихідне поле, якщо значення допустимі
                    continue
            else:
                # Очистити вихідне поле, якщо значення недійсне
                self.output_fields[i].clear()

                # Вивести повідомлення про помилку поруч з відповідним текстовим полем
                self.output_fields[i].setPlainText("❗Рядок не містить масиву.")

        # Перевіряємо, чи є дані для сортування та побудови графіка
        if arrays:
            # Сортування масивів та виведення довжини та часу сортування в консоль
            for array in arrays:
                start_time = time.perf_counter()  # Початок вимірювання часу
                self.binary_insertion_sort(array)
                end_time = time.perf_counter()  # Кінець вимірювання часу
                sorting_time = (end_time - start_time) * 1000  # Переведення часу з секунд у мілісекунди
                times.append((len(array), sorting_time))  # Додаємо довжину масиву та час сортування
                print("Array length:", len(array))
                print("Sorting time:", sorting_time, "milliseconds")

            # Побудова графіка
            self.plot_graph(times)

            # Виведення відсортованих масивів
            for i, array in enumerate(arrays):
                output_field = self.output_fields[i]
                output_field.setPlainText(str(array))
        else:
            print("No arrays to sort.")

    def binary_insertion_sort(self, array):
        # Бінарне вставляння
        for i in range(1, len(array)):
            key = array[i]
            low = 0
            high = i - 1
            while low <= high:
                mid = (low + high) // 2
                if array[mid] < key:
                    low = mid + 1
                else:
                    high = mid - 1
            for j in range(i, low, -1):
                array[j] = array[j-1]
            array[low] = key

    def drag_enter_event(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def drop_event(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            try:
                with open(path, 'r') as file:
                    arrays = []
                    for line in file:
                        if line.strip().startswith('[') and line.strip().endswith(']'):
                            line = line.strip()[1:-1]  # Видаляємо квадратні дужки з початку та кінця рядка
                            numbers = []
                            for val in line.split():
                                try:
                                    num = float(val)
                                    numbers.append(num)
                                except ValueError:
                                    # Якщо значення не може бути конвертоване у float, вивести повідомлення
                                    self.output_fields[0].setPlainText("❗Не числове значення.")
                                    break
                            else:
                                # Якщо всі значення конвертовані у float, додати масив у список для сортування
                                arrays.append(numbers)
                                continue
                        # Очистити вихідне поле, якщо значення недійсне
                            self.output_fields[0].clear()

                        # Вивести повідомлення про помилку поруч з відповідним текстовим полем
                            self.output_fields[0].setPlainText("❗Не числове значення.")

                # Вивід масивів у відповідні текстові поля
                    for i, array in enumerate(arrays):
                        if i < len(self.text_fields):
                            # Роздвляємо масив квадратними дужками [] і розділяємо елементи пробілами
                            formatted_array = "[" + " ".join(map(str, array)) + "]"
                            self.text_fields[i].setText(formatted_array)
            except Exception as e:
                print("Error:", e)

    def plot_graph(self, data):
        lengths, times = zip(*data)
        
        # Апроксимуємо лінію найменших квадратів для вихідних даних
        p = np.polyfit(lengths, times, 3)  # Поліном третього степеня
        new_lengths = np.linspace(min(lengths), max(lengths), 1000)
        new_times = np.polyval(p, new_lengths)
        
        # Обчислення часу за формулою O(n log n) для введених довжин
        log_times = [length * np.log(length) / 1000 for length in new_lengths]  # Переведення мілісекунд в секунди
        
        # Обчислення теоретичного часу сортування для кожної довжини
        theoretical_log_times = [length * np.log(length) / 1000 for length in lengths]  # Переведення мілісекунд в секунди
        
        # Побудова графіків
        plt.figure(figsize=(10, 5))
        
        # Графік вихідних даних (практична залежність)
        plt.subplot(1, 2, 1)
        plt.plot(new_lengths, new_times, color='blue', linestyle='-', linewidth=2)
        plt.scatter(lengths, np.array(times)/10, color='red', marker='o')  # Поділ значень часу на 10
        plt.xlabel('Довжина масиву')
        plt.ylabel('Час сортування (мс)')
        plt.title('Практична залежність')
        plt.grid(True)
        
        # Графік O(n log n) (теоретична залежність)
        plt.subplot(1, 2, 2)
        plt.plot(new_lengths, log_times, color='green', linestyle='-', linewidth=2)
        plt.scatter(lengths, theoretical_log_times, color='red', marker='o')  # Відображаємо точки для теоретичного часу
        plt.xlabel('Довжина масиву')
        plt.ylabel('Час сортування (мс)')
        plt.title('Теоретична залежність')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
