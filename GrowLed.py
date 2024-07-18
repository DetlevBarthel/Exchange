from machine import Pin
from time import sleep
import _thread

class GrowLed:
    def __init__(self,startZeit, endZeit):
        self.LED    = Pin("LED",Pin.OUT)                       # use GP25 as an ouput for the Onboard LED
        self.led_extern = Pin(15, Pin.OUT)
        self.startZeit = startZeit
        self.endZeit = endZeit        
        _thread.start_new_thread(self.blinkLed_continuously, ())

    def blinkLed(self):
        self.led_extern.value(1)
        sleep(1)
        self.led_extern.value(0)
        sleep(1)
    
    def blinkLed_continuously(self):
        while True:
            self.LED.value(1)
            sleep(1)
            self.LED.value(0)
            sleep(1)
    
    def growLed_schalten(self, stunden, minuten,sekunden):
        if (stunden > self.startZeit[0] or (stunden == self.startZeit[0] and minuten >=self.startZeit[1] )) and \
           (stunden < self.endZeit[0] or 
            (stunden == self.endZeit[0] and minuten <=self.endZeit[1])):
            if self.led_extern.value() == 0:
                self.led_extern.value(1)
        else:
            self.led_extern.value(0)
