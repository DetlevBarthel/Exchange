import dht
from machine import Pin
dhtSensor = dht.DHT11(Pin(13))
temp = hum = 0
from time import sleep

class DHT_Sensor:
    def __init__(self):
        self.temp = 0
        self.hum = 0
        print("DHT-Sensor initialisiert")
        sleep(1)
        dhtSensor.measure()
        self.temp = dhtSensor.temperature()  # Temperatur in Celsius
        self.hum = dhtSensor.humidity()  # Luftfeuchtigkeit in Prozent
        print("Temperatur: {}°C, Luftfeuchtigkeit: {}%".format(self.temp, self.hum))
        return [self.temp, self.hum]
    
    def read_temp_hum(self):
        try:
            dhtSensor.measure()
            self.temp = dhtSensor.temperature()  # Temperatur in Celsius
            self.hum = dhtSensor.humidity()  # Luftfeuchtigkeit in Prozent
            print("Temperatur: {}°C, Luftfeuchtigkeit: {}%".format(self.temp, self.hum))
            return [self.temp, self.hum]

        except OSError as e:
            print("Fehler beim Lesen vom DHT11-Sensor: ", e)

        

