import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QGridLayout)
from PyQt6.QtCore import Qt
from light import Light
from switch import Switch

N_CONTROLS = 8

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DIO controller")

        controls_layout = QGridLayout()
        controls_layout.setVerticalSpacing(10)
        controls_layout.setHorizontalSpacing(10)
        controls_layout.setContentsMargins(10, 10, 10, 10)
        self.switches = []
        self.lights = []
        for control in range(N_CONTROLS):
            sw = Switch()
            self.switches.append(sw)
            controls_layout.addWidget(sw, 0, control, Qt.AlignmentFlag.AlignCenter)
            light = Light()
            self.lights.append(light)
            controls_layout.addWidget(light, 1, control, Qt.AlignmentFlag.AlignCenter)
            sw.toggled.connect(
                lambda checked, l=light : (
                    l.set_state(checked)
                ))
        main_layout = QVBoxLayout()
        main_layout.addItem(controls_layout)
        main_layout.addStretch(1)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
