import network
import time
import json
import urequests
from machine import Pin, SoftI2C
import ssd1306

i2c = SoftI2C(scl=Pin(6), sda=Pin(5))  # Adjust the Pin numbers based on your connections
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("Sek Prodi", "sekprodiii")
sta.ifconfig()

def monitor():
	#mengambil data dari accuweather
	r = urequests.get("https://api.openweathermap.org/data/2.5/weather?q=Yogyakarta,id&appid=39860be932e9680238339a90bac4d163&units=metric").json()
	suhu = r['main']['temp']
	kondisi = r['weather'][0]['main']
	city = r['name']
	print("condition: ",kondisi)
	print("Suhu di Tangerang adalah", suhu, "C")
	oled.fill(0)  # Clear the screen
	oled.text("Condition", 0, 15)
	oled.text(kondisi, 0, 25)
	oled.text("local temp:", 0, 35)
	oled.text(str(suhu), 0, 45)
	oled.text(city, 0, 55)
	oled.show()  # Show the text
	time.sleep(10)

while True:	
	monitor()
	
