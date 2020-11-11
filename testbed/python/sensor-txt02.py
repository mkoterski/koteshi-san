#!/usr/bin/env python
#
# Simple test to write readings from a BME280 sensor to a .txt files
# If log file does not exists yet, it will be created
# 
# Last Update: 2020-11-11
# Modified by: Matthias Koterski
#
# Change log: 
# 
# 0.1a - Initial WIP version.
#
# Requirements:
# 1. Raspberry Pi B+ model
# 2. Sensor (BME280)
# 3. Jumper cables
# 4. BME280 library (run "pip3 install RPi.bme280" to install necessary libraries)
#
####################################################################################################################

import time
import os.path
#import board
#import adafruit_dht

#comment and uncomment the lines below depending on your sensor.
#Add use_pulseio=False as Raspberry Pi may not be able to read sensor otherwise

#sensor = Adafruit_DHT.DHT11
sensor = adafruit_dht.DHT22(board.D4, use_pulseio=False) # The sensor is connected to pin #7 / GPIO4
#sensor = Adafruit_DHT.AM2302

#create a variable to control the while loop
running = True

#If sensor_log01.txt does not exist, it will be created. Changing mode from write to append

if os.path.exists("sensor_log02.txt"):
    log_file = open("sensor_log02.txt", "a")
else:
    log_file = open("sensor_log02.txt", "w")
    log_file.write("date, time, temperature (C), humidity\n")

#loop forever
while running:

    try:
        #read the humidity and temperature
        humidity = sensor.humidity
        temperature = sensor.temperature

        #print temperature and humidity to screen
        print(time.strftime("%Y-%m-%d - %H:%M:%S - ") + "Temperature: " + str(temperature) + " °C, " + "Humidity: " + str(humidity) + " %")
        
        #save date, time, temperature in Celsius, and humidity in sensor_log01.txt file
        log_file.write(time.strftime("%Y-%m-%d,%H:%M:%S") + "," + str(temperature) + "," + str(humidity) + "\n")
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