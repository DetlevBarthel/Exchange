import network
import time

class WLan:
    def __init__(self, ssid, pw):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.ssid = ssid
        self.password = pw
        self.max_retries = 10  # Maximale Anzahl von Verbindungsversuchen
        self.ip = 0

    def connect(self):
        retries = 0
        while not self.wlan.isconnected() and retries < self.max_retries:
            print(f"Versuche, eine Verbindung herzustellen... Versuch {retries + 1}")
            self.wlan.connect(self.ssid, self.password)
            timeout = 10  # Wartezeit in Sekunden pro Versuch
            for _ in range(timeout):
                if self.wlan.isconnected():
                    break
                print("Warten auf Verbindung...")
                time.sleep(1)
            if self.wlan.isconnected():
                break
            retries += 1

        if self.wlan.isconnected():
            print("Verbindung hergestellt!")
            print(self.wlan.ifconfig())
            #self.ip = self.wlan.ifconfig()[0]
            #print(f" Verbunden über IP-Adresse:  {self.ip}")
        else:
            print("Konnte keine Verbindung herstellen nach mehreren Versuchen.")
            print("Endgültiger Status:", self.wlan.status())


