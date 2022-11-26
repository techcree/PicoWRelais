# Lets blink LEDs conected with your Raspberry Pi Pico by SKANTA (TechCree) 
#switch the Board LED on or off
# Bibliotheken laden
from machine import Pin
from utime import sleep

# Initialisierung der Onboard-LED
led_onboard = Pin("LED", Pin.OUT)

# LED einschalten
led_onboard.on()

# 5 Sekunden warten
sleep(5)

# LED ausschalten
led_onboard.off()
