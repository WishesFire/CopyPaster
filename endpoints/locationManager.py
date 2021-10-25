from pynput.mouse import Controller
from PIL import ImageGrab


class Location:
    def __init__(self):
        mouse = Controller()
        window = ImageGrab.grab()
        self.mouseX, self.mouseY = mouse.position
        self.windowX, self.windowY = window.size

    # Lower border
    def border(self):
        window_screen_x = list(range(0, 1920))
        position_y1 = list(range(920, 1000))
        position_y2 = list(range(1000, 1080))

        if self.mouseX in window_screen_x and self.mouseY in position_y1:
            self.mouseY -= 40
        elif self.mouseX in window_screen_x and self.mouseY in position_y2:
            self.mouseY -= 150

    # Right border
    def border2(self):
        window_screen_y = list(range(0, 1080))
        position_x1 = list(range(1580, 1813))
        position_x2 = list(range(1813, 1920))

        if self.windowX in position_x1 and self.mouseY in window_screen_y:
            self.windowX -= 190
        elif self.windowX in position_x2 and self.mouseY in window_screen_y:
            self.windowX -= 400


def located(window, locations):
    window.move(locations.mouseX, locations.mouseY)
