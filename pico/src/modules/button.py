from machine import Pin
import time

# TODO Synchronize _ready state

class Button:

    def __init__(self, pin=3, debounce=250):
        self._pin = pin
        self._debounce = debounce
        self._callback = None
        self._button_pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self._ready = True
        self._last_check = -1

        print("Setup Buttton complete")

    def loop(self):
        if not self._ready and self._button_pin.value() == 1:
            self._ready = True

    @property
    def is_pressed(self):
        if not self._ready:
            if self._button_pin.value() == 1:
                self._ready = True
            return False

        if self._button_pin.value() == 0 and time.ticks_diff(time.ticks_ms(), self._last_check) >= self._debounce:
            self._last_check = time.ticks_ms()
            self._ready = False
            return True

        return False