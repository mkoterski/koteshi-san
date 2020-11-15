
#!/usr/bin/python
#
# Originally found at https://tutorials-raspberrypi.de/raspberry-pi-lcd-display-16x2-hd44780/
# Modified to utilise 2 potentiometers to control the displays contrast and brightness

# how to setup an lcd on raspberry pi and programm with python

# LCD Pin    RPi Pin

# D0        40
# D1        38
# D2        36
# D3        32
       



import time
import RPi.GPIO as GPIO

# GPIO association
LCD_RS = 4
LCD_E  = 17
LCD_DATA4 = 18
LCD_DATA5 = 22
LCD_DATA6 = 23
LCD_DATA7 = 24

# Zuordnung der GPIO Pins (ggf. anpassen)
# LCD_RS = 4
# LCD_E  = 17
# LCD_DATA4 = 18
# LCD_DATA5 = 22
# LCD_DATA6 = 23
# LCD_DATA7 = 24

LCD_WIDTH = 16 		# digits per line
LCD_LINE_1 = 0x80 	# adress for the first display row
LCD_LINE_2 = 0xC0 	# adress for the first display row
LCD_CHR = GPIO.HIGH
LCD_CMD = GPIO.LOW
E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_send_byte(bits, mode):
	# Pins auf LOW setzen
	GPIO.output(LCD_RS, mode)
	GPIO.output(LCD_DATA4, GPIO.LOW)
	GPIO.output(LCD_DATA5, GPIO.LOW)
	GPIO.output(LCD_DATA6, GPIO.LOW)
	GPIO.output(LCD_DATA7, GPIO.LOW)
	if bits & 0x10 == 0x10:
	  GPIO.output(LCD_DATA4, GPIO.HIGH)
	if bits & 0x20 == 0x20:
	  GPIO.output(LCD_DATA5, GPIO.HIGH)
	if bits & 0x40 == 0x40:
	  GPIO.output(LCD_DATA6, GPIO.HIGH)
	if bits & 0x80 == 0x80:
	  GPIO.output(LCD_DATA7, GPIO.HIGH)
	time.sleep(E_DELAY)    
	GPIO.output(LCD_E, GPIO.HIGH)  
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, GPIO.LOW)  
	time.sleep(E_DELAY)      
	GPIO.output(LCD_DATA4, GPIO.LOW)
	GPIO.output(LCD_DATA5, GPIO.LOW)
	GPIO.output(LCD_DATA6, GPIO.LOW)
	GPIO.output(LCD_DATA7, GPIO.LOW)
	if bits&0x01==0x01:
	  GPIO.output(LCD_DATA4, GPIO.HIGH)
	if bits&0x02==0x02:
	  GPIO.output(LCD_DATA5, GPIO.HIGH)
	if bits&0x04==0x04:
	  GPIO.output(LCD_DATA6, GPIO.HIGH)
	if bits&0x08==0x08:
	  GPIO.output(LCD_DATA7, GPIO.HIGH)
	time.sleep(E_DELAY)    
	GPIO.output(LCD_E, GPIO.HIGH)  
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, GPIO.LOW)  
	time.sleep(E_DELAY)  

def display_init():
	lcd_send_byte(0x33, LCD_CMD)
	lcd_send_byte(0x32, LCD_CMD)
	lcd_send_byte(0x28, LCD_CMD)
	lcd_send_byte(0x0C, LCD_CMD)  
	lcd_send_byte(0x06, LCD_CMD)
	lcd_send_byte(0x01, LCD_CMD)  

def lcd_message(message):
	message = message.ljust(LCD_WIDTH," ")  
	for i in range(LCD_WIDTH):
	  lcd_send_byte(ord(message[i]),LCD_CHR)
	
if __name__ == '__main__':
	# initialisieren
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(LCD_E, GPIO.OUT)
	GPIO.setup(LCD_RS, GPIO.OUT)
	GPIO.setup(LCD_DATA4, GPIO.OUT)
	GPIO.setup(LCD_DATA5, GPIO.OUT)
	GPIO.setup(LCD_DATA6, GPIO.OUT)
	GPIO.setup(LCD_DATA7, GPIO.OUT)

	display_init()

	
	lcd_send_byte(LCD_LINE_1, LCD_CMD)
	lcd_message("Koteshi-san v0.2")
	lcd_send_byte(LCD_LINE_2, LCD_CMD)
	lcd_message("Auto Gardening")
	
	time.sleep(4)
	
	msg1 = "Koteshi-san v0.2"
	msg2 = "now with display"
	for i in range(len(msg1)):
		lcd_send_byte(LCD_LINE_1, LCD_CMD)
		lcd_message(msg1[:i+1])
		lcd_send_byte(LCD_LINE_2, LCD_CMD)
		lcd_message("")
		time.sleep(0.1)	
	for i in range(len(msg2)):
		lcd_send_byte(LCD_LINE_1, LCD_CMD)
		lcd_message(msg1)
		lcd_send_byte(LCD_LINE_2, LCD_CMD)
		lcd_message(msg2[:i+1])
		time.sleep(0.1)
	
	time.sleep(4)
	
	GPIO.cleanup()