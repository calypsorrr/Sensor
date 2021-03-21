import sensor
import time
import machine

while True:
    sensor.readuart()
    distance = sensor.readout()
    if distance != False:
        print(distance)
