import sensor
import lorawan
import wifi
import time
import wifiada

if lorawan.connect():
    while True:
        sensor.readuart()
        distance = sensor.readout()
        if distance != False:
            lorawan.send(distance)

#wifi.wifi_connect()
#while True:
    #sensor.readuart()
    #distance = sensor.readout()
    #if distance != False:
        #wifiada.sendDataWifi(distance)
