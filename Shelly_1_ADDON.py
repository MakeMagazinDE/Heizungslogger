# Shelly 1 ADDON auslesen
import time
from time import localtime, sleep
from urllib.request import urlopen

SHELLY = 'http://192.168.xxx.xxx/status'     # IP-Adresse vom Shelly 1 ADDON

while True:
    f = urlopen(SHELLY)  # Die Status-Seite des Shelly 1 wird geladen
    shellytext=f.read().decode() # Sie wird in einen String gwandelt
    f.close()
    
    timer = localtime()  # Zeitstempel
    
    liste = shellytext.split('tC":')  # Splitting mit 'tC":' als Trennstring
    sensor1 = liste[1].split(',')     # Aus der liste[1] den Messwert picken
    sensor1[0] = sensor1[0].replace(".",",") # Dezimalpunkt in Komma wandeln
    print("sensor1",timer.tm_sec)               # Ausgabe in Kommandozeile
    print('Vorlauf   : '+str(sensor1[0])+'°C')  # Ausgabe in Kommandozeile

    sensor2 = liste[2].split(',')     # Aus der liste[2] den Messwert picken
    sensor2[0] = sensor2[0].replace(".",",") # Dezimalpunkt in Komma wandeln
    print('sensor2')                            # Ausgabe in Kommandozeile
    print('Ruecklauf : '+str(sensor2[0])+'°C')  # Ausgabe in Kommandozeile

    sensor3 = liste[3].split(',')     # Aus der liste[3] den Messwert picken
    sensor3[0] = sensor3[0].replace(".",",") # Dezimalpunkt in Komma wandeln
    print('sensor3')                            # Ausgabe in Kommandozeile
    print('Warmwasser: '+str(sensor3[0])+'°C')  # Ausgabe in Kommandozeile
    
    datei = time.strftime("%Y_%m_%d_Shelly")+".txt" # Dateinamen generieren
    
    # Datei öffnen und neue Zeile anfügen (ggfls. den Pfad anpassen)
    with open("/home/pi/python_Prog/Shelly_Addon/"+datei, "a") as fh:
            fh.write(time.strftime("%H:%M:%S  ")),
            fh.write((sensor1[0])+"  "+(sensor2[0])+"  "+(sensor3[0])+ "\n")
         
    sleep(5) # Wartezeit von 5 Sekunden
