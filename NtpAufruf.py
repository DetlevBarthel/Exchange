import ntptime
import time

class NtpVerbindung:
    def __init__(self):
        # Zu Anfang des Prorgamms muss die aktuelle Zeit geholt werden
        for _ in range(5):  # Versuchen Sie es bis zu 5 Mal
            try:
                ntptime.settime()
                break
            except Exception as e:
                print(f"Fehler beim Aktualisieren der NTP-Zeit: {e}")
                time.sleep(2)        
        current_time = time.localtime()  
        self.stunden = current_time[3]
        self.minuten = current_time[4]
        self.sekunden = current_time[5]
        self.zeitHolen = 1 # Variable zum Zeitaktualisiern
    

    def update_internetTime(self):
        try:
            current_time = time.localtime()
            current_hour = current_time[3]
            
            if current_hour == 6 and self.zeitHolen == 1:
                for _ in range(5):  # Versuchen Sie es bis zu 5 Mal
                    try:
                        ntptime.settime()
                        break
                    except Exception as e:
                        print(f"Fehler beim Aktualisieren der NTP-Zeit: {e}")
                        time.sleep(2)
                ntptime.settime()
                # Aktuelle Zeit abrufen und als aktuelle Zeit auf der internen
                # Uhr des Pico abspeichern
                current_time = time.localtime()                
                self.stunden = current_time[3]
                self.minuten = current_time[4]
                self.sekunden = current_time[5]
                # Jetzt möchte ich verhindern, dass in dieser Stunde mehrmals die Zeit geholt wird
                self.zeitHolen = 0
                print(f"Zeit erneuert um : {current_time[3]}:{current_time[4]}")

            if current_hour == 7:
                # Der Schalter zum Zeitholen wird wieder angeknipst
                self.zeitHolen = 1

            return current_time[3], current_time[4], current_time[5]
        except Exception as e:
            print(f"Fehler beim Abrufen der NTP-Zeit: {e}")
            return None, None, None

