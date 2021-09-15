from PyQt6 import QtWidgets
import sys
import threading
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyGuiWindow()

    locations = Location()
    locations.border()
    locations.border2()

    located(window, locations)
    window.show()
    threading.Thread(target=show, args=(window, ), daemon=True).start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
