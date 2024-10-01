from machine import Pin
import time

# Define the LED pin
led = Pin(21, Pin.OUT)  # Use correct gpio

# Blink the LED in a loop
while True:
    led.value(1)   # Turn the LED on
    time.sleep(1)  # Wait for a second
    led.value(0)   # Turn the LED off
    time.sleep(1)  # Wait for a second