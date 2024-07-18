from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

class Oled:
    def __init__(self):
        # Display initialisieren
        self.sda_pin = Pin(0)  # Pin 0 für Daten (SDA)
        self.scl_pin = Pin(1)  # Pin 1 für Takt (SCL)
        # SSD1306-Display initialisieren
        self.i2c_ssd1306 = I2C(0, sda=self.sda_pin, scl=self.scl_pin, freq=400000)
        self.ssd1306 = SSD1306_I2C(128, 64, self.i2c_ssd1306)
        '''
        self.ssd1306.fill(0)
        self.ssd1306.text("Test oben", 0, 0)

        self.ssd1306.text("Test unten",0,28)
        self.ssd1306.show()
        '''

    def display(self,anzeigeText,x, y):
        self.ssd1306.text(anzeigeText, x,y)
        self.ssd1306.show()      
        pass