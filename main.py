from PyQt6 import QtWidgets
from gui.design import MyGuiWindow
from endpoints.locationManager import Location
from endpoints.keyboardManager import show
from asyncqt import QEventLoop
import sys
import signal
import asyncio
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')


def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = MyGuiWindow()
        loop = QEventLoop(app)
        asyncio.set_event_loop(loop)

        locations = Location()
        locations.border()
        locations.border2()
        locations.located(window, locations)

        window.show()
        loop.add_signal_handler(signal.SIGINT, window.shutdown, None)
        with loop:
            loop.run_forever(show(window))

        sys.exit(app.exec_())
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
