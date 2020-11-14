#! /usr/bin/env python
# python programa to comunicate with an MCP3008
# Import our SpiDev wrapper and our sleep function

import spidev
from time import sleep

# Establish SPI device on Bus 0,Device 0
spi = spidev.SpiDev()
spi.open(0,0)

def getAdc (channel):
    #check valid channel
    if ((channel>7)or(channel<0)):
        return -1

    # Preform SPI transaction and store returned bits in 'r'
    r = spi.xfer([1, (8+channel) << 4, 0])

    #Filter data bits from retruned bits
    adcOut = ((r[1]&3) << 8) + r[2]
    percent = int(round(adcOut/10.24))

    #print out 0-1023 value and percentage
    print(("ADC Output: {0:4d} Percentage: {1:3}%".format (adcOut,percent)))
    sleep(2.0)

while True:
    getAdc(0)


# SAMPLE OUTPUT
#
# pi@koteshi-san:/koteshi-san/testbed/python $ sudo python3 mcp3008-test01.py
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output: 1023 Percentage: 100%
# ADC Output:  895 Percentage:  87%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output: 1023 Percentage: 100%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output: 1023 Percentage: 100%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  895 Percentage:  87%
# ADC Output:  831 Percentage:  81%
# ADC Output:  991 Percentage:  97%
# ADC Output:    0 Percentage:   0%
# ADC Output:    0 Percentage:   0%
# ADC Output:    0 Percentage:   0%
# ADC Output: 1023 Percentage: 100%
# ADC Output:    0 Percentage:   0%
# ADC Output:    0 Percentage:   0%
# ADC Output:    0 Percentage:   0%
