#!/usr/bin/python
#
# run "pip3 install RPi.bme280" to install necessary libraries
#
# For a data-logger like application, periodically call bme280.sample(bus, address, calibration_params) to get time-based readings.
#

import smbus2
import bme280

#only required for dew point calculation
import math

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# dew point calculation
b = 17.62
c = 243.12
gamma = (b * data.temperature /(c + data.temperature)) + math.log(data.humidity / 100.0)
dew_point = (c * gamma) / (b - gamma)

# the compensated_reading class has the following attributes
print(data.id)
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)
print(dew_point)

# there is a handy string representation too
print(data)