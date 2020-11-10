#!/usr/bin/env python
#
# Simple test to write DHT sensor data to firebase DB
# 
# Last Update: 2020-11-10
# Modified by: Matthias Koterski
#
# Change log: 
# 
# 0.1a - Initial WIP version.
#
# Requirements:
# 1. Raspberry Pi B+ model
# 2. DHT sensor
# 3. Jumper cables
# 4. CircuitPython-DHT library (run "pip3 install adafruit-circuitpython-dht && sudo apt-get install libgpiod2")
# 5. Firebase library (run "pip3 install python-firebase")
# (x. Depending on the sensor model you may need a pull up resistor)
#
####################################################################################################################

import time
#import os.path
import board
import adafruit_dht
from firebase import firebase

#comment and uncomment the lines below depending on your sensor. Here the sensor is connected to pin #7 / GPIO4
#sensor = Adafruit_DHT.DHT11
sensor = adafruit_dht.DHT22(board.D4, use_pulseio=False)
#sensor = Adafruit_DHT.AM2302

#Initialise firebase instance
firebase = firebase.FirebaseApplication("https://koteshi-san.firebaseio.com/", authentication=None)

#create a variable to control the while loop
running = True

#If sensor_log01.txt does not exist, it will be created. Changing mode from write to append

# if os.path.exists("sensor_log01.txt"):
#     log_file = open("sensor_log01.txt", "a")
# else:
#     log_file = open("sensor_log01.txt", "w")
#     log_file.write("date, time, temperature (C), humidity\n")

#loop forever
while running:

    try:
        #read the humidity and temperature
        humidity = sensor.humidity
        temperature = sensor.temperature

        #read the soil moisture
        #soil_moisture = XXXX

        #print temperature and humidity to screen
        print("Temperature: " + str(temperature) + " °C, " + "Humidity: " + str(humidity) + " %")
        
        #save date, time, temperature in Celsius, and humidity in firebase instance
        #log_file.write(time.strftime("%Y-%m-%d,%H:%M:%S") + "," + str(temperature) + "," + str(humidity) + "\n")
        firebase.put("koteshi-san", "Date", time.strftime("%Y-%m-%d"))
        firebase.put("koteshi-san", "Time", time.strftime("%H:%M:%S"))
        firebase.put("koteshi-san", "Temperature in °C", str(temperature))
        firebase.put("koteshi-san", "Humidity", str(humidity))
        #firebase.put("koteshi-san", "Soil Moisture", str(soil_moisture))
        time.sleep(1.0)

    except RuntimeError as error:
    # In case you are interested in the error message you can uncomment the following line
    # Believe me, they are usually not that interesting
    #    print(error.args[0]) 
        time.sleep(2.0)
        continue

    except Exception as error:
        sensor.exit()
        raise error

    except KeyboardInterrupt:
        print ("Program stopped")
        running = False
        log_file.close()

time.sleep(2.0)