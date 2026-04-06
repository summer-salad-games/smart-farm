from src.configurations.config import WIFI_CONFIG
from src.modules.wifi import Wifi
from src.modules.led import Led
from src.modules.dht import DHT
from src.modules.pressure import Pressure
from src.modules.button import Button
from src.modules.ldr import LDR
import machine

class MainController:

    def __init__(self, scl_pin=5, sda_pin=4):
        # self._i2c = machine.I2C(0, scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin), freq=400_000)
        # print(f"I2C components {self._i2c.scan()}")

        self._button = Button()
        self._wifi = Wifi(WIFI_CONFIG["ssid"], WIFI_CONFIG["password"])
        # self._led = Led()
        self._dht = DHT()
        # self._pressure = Pressure(self._i2c, sea_level=1016.5)
        # self._ldr = LDR()

        print("Setup MainController complete")

    def loop(self):
        pass
        # print("--------------------------------- RAW DATA ---------------------------------")
        print(f"DHT22 (Temperature {self._dht.temperature}, Humidity: {self._dht.humidity})")
        # print(f"BMP180 (Pressure {self._pressure.pressure}, Temperature: {self._pressure.temperature}, Altitude: {self._pressure.altitude})")
        # print(f"LDR (Light {self._ldr.brightness})")
        # print(f"Wifi (Connected: {self._wifi.is_connected}, IP: {self._wifi.ip_address})")
        # print(f"Button (Pressed: {self._button.is_pressed})")
        # print("----------------------------------------------------------------------------")