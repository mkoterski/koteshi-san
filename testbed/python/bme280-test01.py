#!/usr/bin/python
#
# run "pip3 install RPi.bme280" to install necessary libraries
#
# For a data-logger like application, periodically call bme280.sample(bus, address, calibration_params) to get time-based readings.
#

import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
print(data.id)
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)

# there is a handy string representation too
print(data)