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

counter = 1 # Set the counter to start at 1

while counter < 11: # While count is less than 11...
#while True:

    print(counter) # Print the current counter
    
    print("Turn On!")
    # LEDs all on
    red.value(1)
    amber.value(1)
    green.value(1)
    
    print("wait...")
    time.sleep(0.5) # Wait half a second
    
    print("Turn Off!")
    # LEDs all off
    red.value(0)
    amber.value(0)
    green.value(0)
    
    print("wait...")
    time.sleep(0.5) # Wait half a second
    
    counter += 1 # Add 1 to our counter

print("Ending awesome program!...BYE :)")