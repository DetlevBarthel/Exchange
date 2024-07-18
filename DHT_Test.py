import machine
import dht
from time import sleep

# Initialisieren des DHT11-Sensors
dht_sensor = dht.DHT11(machine.Pin(16))

def read_temperature():
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        print("Temperatur: {}°C, Luftfeuchtigkeit: {}%".format(temp, hum))
        return temp, hum
    except OSError as e:
        print("Fehler beim Lesen vom DHT11-Sensor: ", e)
        return None, None

# Hauptschleife
while True:
    temp, hum = read_temperature()
    if temp is not None and hum is not None:
        # Veröffentlichen Sie die Werte oder führen Sie andere Aktionen durch
        pass
    sleep(5)
