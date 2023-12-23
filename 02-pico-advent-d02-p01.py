# https://thepihut.com/pages/advent

# Day-2 - https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-2-let-s-get-blinky

from machine import Pin
import time

print("Starting awesome program!...")

# GPIO18 (physical pin 24) for Red
# GPIO19 (physical pin 25) for Amber
# GPIO20 (physical pin 26) for Green

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

print("Turn On!")
red.value(1)
amber.value(1)
green.value(1)

print("wait...")
time.sleep(5)

print("Turn Off!")
red.value(0)
amber.value(0)
green.value(0)

print("Ending awesome program!...BYE :)")