import network, machine, time

class Wifi:
    def __init__(self, ssid, password):
        self._ssid = ssid
        self._password = password
        self._wlan = network.WLAN(network.STA_IF)

        self.connect()
        print("Setup Wifi complete")

    def loop(self):
        pass

    def connect(self, timeout=10):
        self._wlan.active(True)

        if not self.is_connected:
            print(f'Connecting to network {self._ssid}')
            self._wlan.connect(self._ssid, self._password)
            start = time.ticks_ms()
            while not self.is_connected:
                if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
                    print("Connection timed out")
                    return
                machine.idle()

        print(f"Connected to {self._ssid} with IP: {self._wlan.ifconfig()[0]}")

    def disconnect(self):
        if self._wlan.isconnected():
            print("Disconnecting from Wi-Fi...")
            self._wlan.disconnect()
            self._wlan.active(False)
            print("Disconnected from Wi-Fi")
        else:
            print("No active Wi-Fi connection to disconnect")

    @property
    def is_connected(self):
        return self._wlan.isconnected()