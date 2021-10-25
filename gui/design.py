from PyQt5 import QtWidgets, QtCore, QtGui
from config import GUI_SIZE_X, GUI_SIZE_Y, BASE_DIR


class MyGuiWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.MSWindowsFixedSizeDialogHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet('background-color: #B0E0E6;')
        self.resize(GUI_SIZE_X, GUI_SIZE_Y)

        self.hbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.hbox)

        self.clipboard = QtWidgets.QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.detect_clipboard_duplication)

        self.scroll = QtWidgets.QScrollArea()
        self.hbox.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedHeight(150)
        self.scrollContent = QtWidgets.QWidget(self.scroll)
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.scroll_layout)
        self.scroll.setWidget(self.scrollContent)

        # Icon
        self.setWindowIcon(QtGui.QIcon(BASE_DIR + '\\logo\\Icon2.png'))

        self.tray = QtWidgets.QSystemTrayIcon(self)
        self.tray.setIcon(QtGui.QIcon(BASE_DIR + '\\logo\\Icon2.png'))

        show_action = QtWidgets.QAction('Show', self)
        quit_action = QtWidgets.QAction('Exit', self)
        hide_action = QtWidgets.QAction('Hide', self)
        inform_action = QtWidgets.QAction('Information', self)

        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        inform_action.triggered.connect(self.info)
        quit_action.triggered.connect(QtWidgets.qApp.quit)

        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(inform_action)
        tray_menu.addAction(quit_action)

        self.tray.setContextMenu(tray_menu)
        self.tray.show()

    def detect_clipboard_duplication(self):
        out = ''
        total_part = 50
        total_word = len(self.clipboard.text())

        if total_word > total_part:
            for part in range(total_word // total_part):
                out += f"{part[:total_part]}\n{part[total_part:]}"
            out += "\n"
        else:
            out = self.clipboard.text()

        button = QtWidgets.QPushButton(out)
        button.clicked.connect(self.button_func)
        self.scroll_layout.addWidget(button)

    def button_func(self):
        sender = self.sender()
        self.clipboard.setText(sender.text())
        self.hide()

    def info(self):
        QtWidgets.QMessageBox.about(self, "About program",
                                          "<center>\"CopyPaster\" v2.0<br><br>"
                                          "A program for viewing your copy list and using them<br><br>"
                                          "(c) Vojtsitskiy Maksym, 2020")
        self.show()

    def closeEvent(self, evt):
        evt.ignore()
        self.hide()
