import pyautogui
from PyQt6 import QtWidgets, QtCore, QtGui
import os
import sys
from pynput import keyboard
import threading


class MyGuiWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(
            QtCore.Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet('background-color: #B0E0E6;')
        self.resize(400, 150)

        self.buttonlist = []
        self.hbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.hbox)

        self.clipboard = QtWidgets.QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.detectClipboard)

        self.scroll = QtWidgets.QScrollArea()
        self.hbox.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedHeight(150)
        self.scrollContent = QtWidgets.QWidget(self.scroll)
        self.scrolllayout = QtWidgets.QVBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.scrolllayout)

        self.scroll.setWidget(self.scrollContent)

        # Icon
        self.path = os.path.abspath(os.curdir)
        self.setWindowIcon(QtGui.QIcon(str(self.path) + '\\logo\\Icon2.png'))

        self.tray = QtWidgets.QSystemTrayIcon(self)
        self.tray.setIcon(QtGui.QIcon(str(self.path) + '\\logo\\Icon2.png'))

        show_action = QtWidgets.QAction('Show', self)
        quit_action = QtWidgets.QAction('Exit', self)
        hide_action = QtWidgets.QAction('Hide', self)
        inform_action = QtWidgets.QAction('Information', self)

        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        inform_action.triggered.connect(self.aboutinfo)
        quit_action.triggered.connect(QtWidgets.qApp.quit)

        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(inform_action)
        tray_menu.addAction(quit_action)

        self.tray.setContextMenu(tray_menu)
        self.tray.show()

    def detectClipboard(self):
        self.out = ''
        self.total = 0
        self.totals = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]

        if len(self.clipboard.text()) > 100:
            for i in self.clipboard.text():
                self.total += 1
                if self.total in self.totals:
                    self.out += i + '\n'
                else:
                    self.out += i
        else:
            self.out = self.clipboard.text()

        if self.out not in self.buttonlist:

            self.button = QtWidgets.QPushButton(self.out)
            self.button.clicked.connect(self.button_func)
            self.buttonlist.append(self.out)
            self.scrolllayout.addWidget(self.button)
        else:
            pass

    def button_func(self):
        sender = self.sender()
        self.clipboard.setText(sender.text())
        self.hide()

    def aboutinfo(self):
        QtWidgets.QMessageBox.about(self, 'About program',
                                    "<center>\"CopyPaster\" v1.5.5<br><br>"
                                    "A program for viewing your copy list and using them<br><br>"
                                    "(c) Vojtsitskiy Maksym, 2020")
        self.show()

    def closeEvent(self, evt):
        evt.ignore()
        self.hide()


# Class Location of the window
class Location:
    def __init__(self):
        self.MouseX, self.MouseY = pyautogui.position()
        self.WindowX, self.WindowY = pyautogui.size()

    # Lower border
    def border(self):
        self.POSITIONERX = list(range(0, 1920))
        self.positionerY1 = list(range(920, 1000))
        self.positionerY2 = list(range(1000, 1080))

        if self.MouseX in self.POSITIONERX and self.MouseY in self.positionerY1:
            self.MouseY = self.MouseY - 40
        elif self.MouseX in self.POSITIONERX and self.MouseY in self.positionerY2:
            self.MouseY = self.MouseY - 150

    # Right border
    def border2(self):
        self.POSITIONERY = list(range(0, 1080))
        self.positionerX1 = list(range(1580, 1813))
        self.positionerX2 = list(range(1813, 1920))

        if self.MouseX in self.positionerX1 and self.MouseY in self.POSITIONERY:
            self.MouseX = self.MouseX - 190
        elif self.MouseX in self.positionerX2 and self.MouseY in self.POSITIONERY:
            self.MouseX = self.MouseX - 400


# Function control press
def show(window):
    Comb = [{keyboard.KeyCode(char='~')},  # Caps ~ (EU)
            {keyboard.KeyCode(char='`')},  # `` (EU)
            {keyboard.KeyCode(char='₴')},  # ₴ (UA)
            {keyboard.KeyCode(char="'")},  # ' (UA)
            {keyboard.KeyCode(char="ё")},  # ё (RU)
            {keyboard.KeyCode(char="Ё")}]  # Ё (RU)

    def get_key_name(key):

        if isinstance(key, keyboard.KeyCode):
            return key.char
        else:
            return str(key)

    def on_press(key):

        if key == keyboard.Key.esc:
            window.hide()

        elif (key == keyboard.KeyCode.from_char('`')) or \
                (key == keyboard.KeyCode.from_char('~')) or \
                (key == keyboard.KeyCode.from_char('₴')) or \
                (key == keyboard.KeyCode.from_char('ё')) or \
                (key == keyboard.KeyCode.from_char('Ё')):

            locations = Location()
            locations.border()
            locations.border2()
            located(window, locations)

            window.show()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


# Function for located window
def located(window, locations):
    window.move(locations.MouseX, locations.MouseY)


# Command function
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyGuiWindow()

    locations = Location()
    locations.border()
    locations.border2()

    located(window, locations)

    window.show()
    threading.Thread(target=show, args=(window,), daemon=True).start()

    sys.exit(app.exec_())


main()