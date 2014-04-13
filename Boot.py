#!/usr/bin/python

from Modulos.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep
import commands

lcd = Adafruit_CharLCDPlate()
lcd.clear()

for i in range(5):
	lcd.message(".")
	sleep(0.5)

def salir():
	lcd.clear()	
	lcd.message("Quieres salir?\n")
	lcd.message(" Si <-   -> No ")
	while True:
		if lcd.buttonPressed(lcd.LEFT):
			lcd.clear()
			sleep(0.4)
			lcd.message("saliendo......")
			sleep(0.7)
			lcd.backlight(lcd.OFF)
			lcd.noDisplay()
			exit()
		if lcd.buttonPressed(lcd.RIGHT):
			lcd.clear()
			sleep(0.4)
			lcd.message("ok")
			return

def Wellcome():
	lcd.clear()
	lcd.message("Raspberri Pi!")
	lcd.backlight(lcd.VIOLET)

Wellcome()

while True:
	if lcd.buttonPressed(lcd.DOWN):
		lcd.clear()
		sleep(0.4)
		eth0 = commands.getoutput("/sbin/ifconfig eth0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'")
		if not eth0:
			lcd.message ("eth0 no tiene IP")
		else:
			lcd.message (eth0+"\n wlan0")
		lcd.backlight(lcd.GREEN)
	if lcd.buttonPressed(lcd.UP):
		lcd.clear()
		sleep(0.4)
		wlan0 = commands.getoutput("/sbin/ifconfig wlan0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'")
		if not wlan0:
			lcd.message ("wlan0 no pose IP")
		else:
			lcd.message (wlan0+"\n    wlan0")
		lcd.backlight(lcd.GREEN)
	if lcd.buttonPressed(lcd.RIGHT):
		lcd.clear()
		sleep(0.4)
		Wellcome()
	if lcd.buttonPressed(lcd.SELECT):
		lcd.clear()
		sleep(0.4)
		salir()
		Wellcome()








