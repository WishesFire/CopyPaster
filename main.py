from PyQt5 import QtWidgets
from gui.design import MyGuiWindow
from endpoints.locationManager import Location, located
from endpoints.keyboardManager import show
import threading
import sys


def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = MyGuiWindow()

        locations = Location()
        locations.border()
        locations.border2()
        located(window, locations)

        window.show()
        threading.Thread(target=show, args=(window,), daemon=True).start()
        sys.exit(app.exec_())

    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
