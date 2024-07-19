import time
import urequests


class Https:
    def __init__(self):
        self.zeit = 0
        
        
    def update_internetTime(self):
        response = urequests.get('https://timeapi.io/api/Time/current/zone?timezone=Europe/Berlin')
        while response.status_code!=200:
            response = urequests.get('https://timeapi.io/api/Time/current/zone?timezone=Europe/Berlin')
            time.sleep(1)
            print("Fehler beim Abrufen der Uhrzeit: " ,response.status_code)
            response.close()
        if response.status_code == 200:
           data = response.json()
           current_time = data['time']
           sekunden = str(round(data['seconds'],1))
           self.zeit = current_time + ":" + sekunden