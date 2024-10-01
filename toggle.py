from machine import Pin


led_red = Pin(21, Pin.OUT)
push_btn = Pin(2, Pin.IN, Pin.PULL_UP)


def handle_toggle(pin):
    led_red.value(not led_red.value())


push_btn.irq(handle_toggle, trigger=Pin.IRQ_RISING)