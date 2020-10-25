pump-poc.py

import RPi.GPIO as GPIO       	# Import required Python libraries
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
from Tkinter import*
myGui=Tk()
while True:
	def onlamp():
		GPIO.output(7,True)
	def offlamp():
		GPIO.output(7,False)
	myGui.title("Hello")
	myGui.geometry("200x350+200+200")
	while True:
		myButton1=Button(text='on',fg='black',bg='green',command=onlamp).pack()
		myButton2=Button(text='off',fg='black',bg='green',command=offlamp).pack()
		myGui.mainloop()
	