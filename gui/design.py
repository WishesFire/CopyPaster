from PyQt6 import QtWidgets, QtCore
from config import GUI_SIZE_X, GUI_SIZE_Y


class MyGuiWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.MSWindowsFixedSizeDialogHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet('background-color: #B0E0E6;')
        self.resize(GUI_SIZE_X, GUI_SIZE_Y)
        self.button_list = []
        box = QtWidgets.QVBoxLayout()
        self.setLayout(box)
