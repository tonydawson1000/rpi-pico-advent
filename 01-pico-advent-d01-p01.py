# https://thepihut.com/pages/advent

# Day-1 - https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-1-getting-started

from machine import Pin
import time

print("This is my Pico talking")

# GPIO25 -a little LED onboard
onboardLED = Pin(25, Pin.OUT)

# inputs - we send signals/voltage in to the Pico (button or a sensor)
# outputs - the Pico sends signals/voltage out to something (LEDs or buzzers)

print("Starting awesome program!...")

print("Turn On!")
onboardLED.value(1)

print("wait...")
time.sleep(5)

print("Turn Off!")
onboardLED.value(0)

print("Ending awesome program!...BYE :)")