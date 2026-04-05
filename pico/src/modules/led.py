import machine

class Led:
    def __init__(self, pin="LED"):
        self._pin = pin
        self._led = machine.Pin(self._pin, machine.Pin.OUT)
        
        print("Setup LED complete")

    def loop(self):
        pass

    def on(self):
        self._led.on()

    def off(self):
        self._led.off()

    def toggle(self):
        self._led.toggle()