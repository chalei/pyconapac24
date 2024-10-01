import network
import time
import json
import urequests
import machine

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("Sek Prodi", "sekprodiii")
sta.ifconfig()

def monitor():
	#mengambil data dari accuweather
	r = urequests.get("https://api.openweathermap.org/data/2.5/weather?q=Yogyakarta,id&appid=<token>&units=metric").json()
	suhu = r['main']['temp']
	kondisi = r['weather'][0]['main']
	city = r['name']
	print("condition: ",kondisi)
	print("todays temp in", city, "is", suhu, "C")
    #print(dataRelay)
	time.sleep(10)

while True:	
	monitor()
	
