from network import WLAN
import machine
import pycom
import time
pycom.heartbeat(False)
wlan = WLAN(mode=WLAN.STA)

wlan.connect(ssid="devolo-ae8", auth=(WLAN.WPA2, 'EDVJCYKSJWMEGHZH'))
while not wlan.isconnected():
    pycom.rgbled(0xFF0000)
print("WiFi connected succesfully")
pycom.rgbled(0x00FF00)
time.sleep(2)
print(wlan.ifconfig())
