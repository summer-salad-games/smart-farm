import network, machine, time

class Wifi:
    def __init__(self, ssid, password, retries=3):
        self._ssid = ssid
        self._password = password
        self._wlan = network.WLAN(network.STA_IF)
        self._retries = retries
        self._tries = 0

        self._try_connect()

        print("Setup Wifi complete")

    def connect(self, timeout=15):
        self._wlan.active(True)

        if not self.is_connected:
            print(f'Connecting to network {self._ssid}')
            self._wlan.connect(self._ssid, self._password)
            start = time.ticks_ms()
            while not self.is_connected:
                if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
                    return False
                machine.idle()

        if self.is_connected:
            print(f"Connected to {self._ssid} with IP: {self.ip_address}")
        else:
            print(f"Failed to connect to {self._ssid}")

        return self.is_connected

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
    
    @property
    def ip_address(self):
        if self.is_connected:
            return self._wlan.ifconfig()[0]
        return None
    
    def _try_connect(self):
        while not self.is_connected and self._tries < self._retries:
            if self._tries > 0:
                self._wlan.disconnect()

            if self.connect():
                break
            else:
                print(f"Retrying Wi-Fi connection ({self._tries + 1}/{self._retries})")
                self._tries += 1
        
        if not self.is_connected:
            print("Failed to connect to Wi-Fi after multiple attempts")