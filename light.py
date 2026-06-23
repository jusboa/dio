""" Input indicator - LED like widget. """
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QRadialGradient
from PyQt6.QtCore import Qt

class Light(QWidget):
    """ Rounded light widget that could be turned on/off. """
    def __init__(self, parent=None, is_on=False):
        super().__init__(parent)
        self.is_on = is_on
        self.setFixedSize(50, 70)

    def set_state(self, state):
        """ Turn the light on/off. """
        self.is_on = state
        self.update()

    def paintEvent(self, _event):
        """ Overriden method to draw a light
        emitting or being off based on last set_state(). """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Coordinates
        center_x, center_y = self.width() // 2, 25
        radius = 20

        # Draw light shape
        color = QColor(255, 255, 100) if self.is_on else QColor(150, 150, 150)
        painter.setPen(QPen(color, 2))
        painter.setBrush(color)
        painter.drawEllipse(center_x - radius, center_y - radius, radius*2, radius*2)

        # Draw light glow (if on)
        if self.is_on:
            glow = QRadialGradient(center_x, center_y, radius)
            glow.setColorAt(0, QColor("yellow"))
            glow.setColorAt(1, QColor(255, 215, 0)) # light gold
            painter.setBrush(glow)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(center_x - radius, center_y - radius, radius*2, radius*2)
