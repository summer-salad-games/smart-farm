import machine
from src.utils.math_utils import MathUtils

class LDR:
    def __init__(self, pin=26, max_value=64900, min_value=250):
        self._max_value = max_value
        self._min_value = min_value
        self._pin = pin
        self._adc = machine.ADC(self._pin)
        print("Setup LDR complete")

    def loop(self):
        pass

    @property
    def brightness(self):
        raw = self._adc.read_u16()
        brightness = MathUtils.map(raw, self._min_value, self._max_value, flipped=True)
        return int(brightness)