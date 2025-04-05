import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QRadioButton, QCheckBox, \
    QListWidget, QSlider, QComboBox, QAction, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Лаба 1')
        self.setGeometry(300, 300, 800, 600)
        self.timer_count = 0

        self.create_menu()
        self.create_text_input()
        self.create_buttons()
        self.create_color_controls()
        self.create_list_widget()
        self.create_slider()
        self.create_combo_box()
        self.create_timer()
        self.create_reset_timer_button()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Файл")
        help_menu = menubar.addMenu("Справка")

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        about_action = QAction("О программе", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

    def create_text_input(self):
        self.label_input = QLabel("Введите текст:", self)
        self.label_input.setGeometry(50, 20, 300, 30)

        self.text_input = QLineEdit(self)
        self.text_input.setGeometry(50, 50, 300, 30)
        self.text_input.setText('Пример ввода текста')

        self.label_output = QLabel("Вывод текста:", self)
        self.label_output.setGeometry(50, 160, 300, 30)

    def create_buttons(self):
        self.button = QPushButton("Вывести текст", self)
        self.button.setGeometry(50, 100, 300, 40)
        self.button.clicked.connect(self.on_button_click)

    def create_color_controls(self):
        self.color_block = QLabel(self)
        self.color_block.setGeometry(400, 50, 150, 150)
        self.color_block.setStyleSheet("background-color: gray; border: 1px solid black;")

        self.red_button = QRadioButton("Красный", self)
        self.red_button.setGeometry(400, 220, 100, 30)
        self.red_button.clicked.connect(lambda: self.change_color("red"))

        self.green_button = QRadioButton("Зелёный", self)
        self.green_button.setGeometry(500, 220, 100, 30)
        self.green_button.clicked.connect(lambda: self.change_color("green"))

        self.blue_button = QRadioButton("Синий", self)
        self.blue_button.setGeometry(600, 220, 100, 30)
        self.blue_button.clicked.connect(lambda: self.change_color("blue"))

        self.border_checkbox = QCheckBox("Рамка блока", self)
        self.border_checkbox.setGeometry(400, 260, 150, 30)
        self.border_checkbox.setChecked(False)
        self.border_checkbox.stateChanged.connect(self.toggle_border)

    def create_list_widget(self):
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(50, 200, 200, 100)
        self.list_widget.addItems(["Элемент 1", "Элемент 2", "Элемент 3"])
        self.list_widget.itemClicked.connect(self.on_item_click)

    def create_slider(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(50, 350, 200, 30)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.on_slider_change)

    def create_combo_box(self):
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(50, 400, 200, 30)
        self.combo_box.addItems(["Вариант 1", "Вариант 2", "Вариант 3"])
        self.combo_box.currentIndexChanged.connect(self.on_combo_change)

    def create_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer_label)
        self.timer.start(2000)

        self.timier_label_output = QLabel(f"Таймер сработал {self.timer_count} раз", self)
        self.timier_label_output.setGeometry(400, 330, 300, 30)

    def create_reset_timer_button(self):
        self.timer_button = QPushButton("Сбросить счетчик таймера", self)
        self.timer_button.setGeometry(400, 370, 300, 30)
        self.timer_button.clicked.connect(self.reset_timer_button)

    def on_button_click(self):
        text = self.text_input.text()
        self.label_output.setText(f"Введенный текст: {text}")

    def change_color(self, color):
        colors = {
            "red": "background-color: red; border: 1px solid black;",
            "green": "background-color: green; border: 1px solid black;",
            "blue": "background-color: blue; border: 1px solid black;"
        }
        self.color_block.setStyleSheet(colors[color])

    def toggle_border(self, state):
        if state == 2:
            self.color_block.setStyleSheet(self.color_block.styleSheet() + "border: 10px solid black;")
        else:
            self.color_block.setStyleSheet(self.color_block.styleSheet().replace("border: 10px solid black;", ""))

    def on_item_click(self, item):
        self.label_output.setText(f"Выбран: {item.text()}")

    def on_slider_change(self):
        value = self.slider.value()
        self.label_output.setText(f"Значение слайдера: {value}")

    def on_combo_change(self):
        selected = self.combo_box.currentText()
        self.label_output.setText(f"Выбранный вариант: {selected}")

    def show_about_dialog(self):
        QMessageBox.information(self, "О программе", "Это лабораторная работа 1 по GUI")

    def update_timer_label(self):
        self.timer_count += 1
        self.timier_label_output.setText(f"Таймер сработал {self.timer_count} раз")

    def reset_timer_button(self):
        self.timer_count = 0
        self.timier_label_output.setText(f"Таймер сработал {self.timer_count} раз")

    def mouseMoveEvent(self, event):
        self.label_output.setText(f"Мышь: {event.x()}, {event.y()}")

    def keyPressEvent(self, event):
        self.label_output.setText(f"Клавиша: {event.text()}")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(255, 0, 0))
        painter.setBrush(QColor(0, 255, 0))
        painter.drawRect(400, 500, 300, 30)

    def resizeEvent(self, event):
        new_width = event.size().width()
        new_height = event.size().height()
        self.label_output.setText(f"Размер окна: {new_width}x{new_height}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())