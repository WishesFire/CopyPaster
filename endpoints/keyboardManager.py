from pynput import keyboard
from endpoints.locationManager import Location
from config import KEYBOARD_COMBO


async def show(window):
    async def get_key_name(key):
        if isinstance(key, keyboard.KeyCode):
            return key.char
        return None

    async def on_press(key):
        if key == keyboard.Key.esc:
            window.hide()
        key_press = await get_key_name(key)

        if key_press in KEYBOARD_COMBO:
            locations = Location()
            locations.border()
            locations.border2()
            locations.located(window, locations)

            window.show()

    async with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
