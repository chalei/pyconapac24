import time
from machine import Pin, I2C
import ssd1306
#import math

# ESP8266 Pin assignment
i2c = I2C(scl=Pin(6), sda=Pin(5))  # Adjust the Pin numbers based on your connections
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)  # Clear the screen
oled.text("Pycon APAC 2024", 0, 15)
oled.text("see u in jogja", 0, 35)
oled.text("(`3`)y", 30, 55)
oled.show()  # Show the text