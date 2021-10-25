from pynput import keyboard
from endpoints.locationManager import Location, located
from config import KEYBOARD_COMBO


def show(window):
    def get_key_name(key):
        if isinstance(key, keyboard.KeyCode):
            return key.char
        return None

    def on_press(key):
        if key == keyboard.Key.esc:
            window.hide()
        key_press = get_key_name(key)

        if key_press in KEYBOARD_COMBO:
            locations = Location()
            locations.border()
            locations.border2()
            located(window, locations)

            window.show()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
