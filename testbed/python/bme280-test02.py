#!/usr/bin/python
#
# run "pip3 install RPi.bme280" to install necessary libraries

# pi@koteshi-san:~ $ sudo pip3 install RPi.bme280
# Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
# Collecting RPi.bme280
#   Downloading RPi.bme280-0.2.3-py2.py3-none-any.whl (10 kB)
# Collecting smbus2
#   Downloading https://www.piwheels.org/simple/smbus2/smbus2-0.3.0-py2.py3-none-any.whl (9.1 kB)
# Installing collected packages: smbus2, RPi.bme280
# Successfully installed RPi.bme280-0.2.3 smbus2-0.3.0

# For a data-logger like application, periodically call bme2.sample(bus, address, calibration_params) to get time-based readings.

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