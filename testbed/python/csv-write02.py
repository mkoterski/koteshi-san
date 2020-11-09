#!/usr/bin/python
# based on script originally posted on https://github.com/geektechdude/temperature_project/blob/master/write_readings_to_csv
# Sensor to CSV

# initial set up of imports

import time
import datetime

import board
import adafruit_dht

# gpiozero for CPU
#from gpiozero import CPUTemperature

# imports the modules for the sensor
# from bmp280 import BMP280
# try:
#     from smbus2 import SMBus
# except ImportError:
#     from smbus import SMBus
    
# lux sensor
#import ltr559

# csv to be able to open file
import csv

# sets up the variables for the sensor
# bus=SMBus(1)
# bmp280 = BMP280(i2c_dev=bus)

# functions to use

# def cpu_temperature():
#     cpu = CPUTemperature()
#     cpu_temp = cpu.temperature
#     cpu_temp = str(cpu_temp)
#     return(cpu_temp)


# Initial the dht device, with data pin connected to:
#dhtDevice = adafruit_dht.DHT22(board.D4)
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)


def get_temp():
    temperature_c = dhtDevice.temperature
    temperature_c = str(temperature_c)
    return(temperature)

def get_humidity():
	humidity = dhtDevice.humidity
	humidity = str(humidity)
	return(humidity)

# def get_pressure():
#     pressure = bmp280.get_pressure()
#     pressure = round(pressure)
#     pressure = str(pressure)
#     return(pressure)

# def get_lux():
#     lux = ltr559.get_lux()
#     for x in range(1,5):
#         x_lux = lux
#         time.sleep(0.5)
#     lux_rounded = round(x_lux,2)
#     lux_str = str(lux_rounded)
#     return(lux_str)

def date_now():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today = str(today)
    return(today)

def time_now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    now = str(now)
    return(now)

def write_to_csv():
    # the a is for append, if w for write is used then it overwrites the file
    with open('/sensor_readings_test.csv', mode='a') as sensor_readings_test:
        sensor_write = csv.writer(sensor_readings_test, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_to_log = sensor_write.writerow([date_now(),time_now(),get_temp(),get_humidity()])
      #  write_to_log = sensor_write.writerow([date_now(),time_now(),get_temp(),get_pressure(),get_lux(),cpu_temperature()])
        return(write_to_log)

write_to_csv()