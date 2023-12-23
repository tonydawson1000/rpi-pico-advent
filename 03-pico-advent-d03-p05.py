# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
greenButton = Pin(13, Pin.IN, Pin.PULL_DOWN)
amberButton = Pin(8, Pin.IN, Pin.PULL_DOWN)
redButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

#Start with All Off
red.value(0) # red LED off
amber.value(0) # amber LED off
green.value(0) # green LED off

while True: # Loop forever

    time.sleep(0.3) # Short delay
            
    if redButton.value() == 1: #If button 1 (redButton) is pressed
        
        print("Button 1 (redButton) pressed")
        
        red.toggle() # Toggle Red LED on/off
        
    elif amberButton.value() == 1: # If button 2 (amberButton) is pressed
        
        print("Button 2 (amberButton) pressed")
        
        amber.toggle() # Toggle Amber LED on/off

    elif greenButton.value() == 1: # If button 3 (greenButton) is pressed
        
        print("Button 3 (greenButton) pressed")
        
        green.toggle() # Toggle Green LED on/off