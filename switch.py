""" Output indicator - slide on/off switch widget."""
from PyQt6.QtCore import (
    Qt,
    QPropertyAnimation,
    pyqtProperty,
    QEasingCurve)
from PyQt6.QtGui import (
    QPainter,
    QColor,
    QBrush)
from PyQt6.QtWidgets import QCheckBox

class Switch(QCheckBox):
    """ When clicked the widget changes its
    state. The state change is animated and the
    current state is indicated by green (on) or gray (off)
    background. """
    def __init__(self, parent=None):
        super().__init__(parent)

        # Track the horizontal position of the slider circle
        self._handle_position = 3

        self.setFixedSize(60, 28)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._bg_color_unchecked = QColor(204, 204, 204) # light gray
        self._bg_color_checked = QColor(50, 205, 50)   # lime
        self._handle_color = QColor("white")

        # Define the slide animation
        self.animation = QPropertyAnimation(self, b"handle_position", self)
        self.animation.setDuration(200) # milliseconds
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        # Trigger animation when toggled
        self.clicked.connect(self.setup_animation)

    def hitButton(self, _pos):
        """ Overriden QCheckBox method to define
        which widget area is clickable. Return True
        to make clickable the entire widget. """
        return True

    @pyqtProperty(float)
    def handle_position(self):
        """ Define a Qt property so QPropertyAnimation
        can smoothly slide the handle. """
        return self._handle_position

    @handle_position.setter
    def handle_position(self, pos):
        """ Callback to get the current slider position
        withing the widget during the animation.
        Triggers the widget update. """
        self._handle_position = pos
        self.update()

    def setup_animation(self, checked):
        """ Prepare and start tha slider animation. """
        self.animation.stop()
        if checked:
            self.animation.setEndValue(self.width() - self.height() + 3)
        else:
            self.animation.setEndValue(3)
        self.animation.start()

    def paintEvent(self, _event):
        """ Overriden method to draw a widget. """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw background capsule track
        if self.isChecked():
            painter.setBrush(QBrush(self._bg_color_checked))
        else:
            painter.setBrush(QBrush(self._bg_color_unchecked))

        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0,
                                self.width(),
                                self.height(),
                                self.height() / 2,
                                self.height() / 2)

        # Draw moving slider circle
        painter.setBrush(QBrush(self._handle_color))
        circle_diameter = self.height() - 6
        painter.drawEllipse(int(self._handle_position), 3, circle_diameter, circle_diameter)
        painter.end()
