from machine import Pin
import time

class Button:

    def __init__(self, pin=3, debounce=50):
        self._pin = pin
        self._debounce = debounce
        self._button_pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self._debounced_state = False
        self._last_state = False
        self._last_time = time.ticks_ms()

        print("Setup Button complete")

    @property
    def is_pressed(self):
        current = self._button_pin.value() == 0
        now = time.ticks_ms()
        if current != self._last_state:
            self._last_state = current
            self._last_time = now
        elif time.ticks_diff(now, self._last_time) >= self._debounce:
            self._debounced_state = current
        return self._debounced_state