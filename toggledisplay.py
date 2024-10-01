from machine import Pin, SoftI2C
import ssd1306
import time


i2c = SoftI2C(scl=Pin(6), sda=Pin(5))  # Adjust the Pin numbers based on your connections
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

led_red = Pin(21, Pin.OUT)
push_btn = Pin(2, Pin.IN, Pin.PULL_UP)


def handle_toggle(pin):
    oled.fill(0)  # Clear the screen
    oled.text("led state:", 10, 15)
    oled.text(str(led_red.value()), 10, 25)
    oled.show()
    led_red.value(not led_red.value())


push_btn.irq(handle_toggle, trigger=Pin.IRQ_RISING)
