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
import smbus2
import bme280

#only required for dew point calculation
import math

#connection parameters
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

#create a variable to control the while loop
running = True

#If sensor_log01.txt does not exist, it will be created. Changing mode from write to append

if os.path.exists("sensor_log02.txt"):
    log_file2 = open("sensor_log02.txt", "a")
else:
    log_file2 = open("sensor_log02.txt", "w")
    log_file2.write("date, time, temperature (C), air pressure hPa, humidity rH, \n")

#loop forever
while running:

    try:
        #read the humidity and temperature

        data = bme280.sample(bus, address, calibration_params)

        # dew point calculation
        b = 17.62
        c = 243.12
        gamma = (b * data.temperature /(c + data.temperature)) + math.log(data.humidity / 100.0)
        dew_point = (c * gamma) / (b - gamma)

        # read metrics
        humidity = data.humidity
        temperature = data.temperature
        pressure = data.pressure

        #print temperature, pressure, and humidity to screen
        print(time.strftime("%Y-%m-%d - %H:%M:%S - ") + "Temperature: " + str(temperature) + " °C, " + "Pressure: " + str(pressure) + " hPa, " + "Humidity: " + str(humidity) + " % ")
        
        #save date, time, temperature in Celsius, and humidity in sensor_log01.txt file
        log_file2.write(time.strftime("%Y-%m-%d,%H:%M:%S") + "," + str(temperature) + "," + str(pressure) + "," + str(humidity) + "\n")
        time.sleep(1.0)

    except RuntimeError as error:
    # In case you are interested in the error message you can uncomment the following line
    # Believe me, they are usually not that interesting
    #    print(error.args[0]) 
        time.sleep(2.0)
        continue

    except Exception as error:
        calibration_params.exit()
        raise error

    except KeyboardInterrupt:
        print ("Program stopped")
        running = False
        log_file2.close()

time.sleep(2.0)