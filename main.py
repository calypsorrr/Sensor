import sensor
import lorawan
import wifi
import time
import wifiada
from pysense import Pysense
import machine

if lorawan.connect():
    while True:
        sensor.readuart()
        distance = sensor.readout()
        if distance != False:
            lorawan.send(distance)
            machine.sleep(3000*10, True)
            lorawan.connect()

#wifi.wifi_connect()
#while True:
    #sensor.readuart()
    #distance = sensor.readout()
    #if distance != False:
        #wifiada.sendDataWifi(distance)
