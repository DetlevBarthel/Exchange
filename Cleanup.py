import gc
from machine import WDT

class Putzmann:
    def __init__(self, timeout=8000):
        # Watchdog Timer mit einer Timeout-Zeit initialisieren
        #self.wdt = WDT(timeout=timeout)
        pass
    
    def putzen(self):
        # Garbage Collection durchführen und Watchdog Timer füttern
        gc.collect()
        #self.wdt.feed()
        return str(gc.mem_free()) # Zeigt den freien Speicher an
