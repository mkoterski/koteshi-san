
#! /usr/bin/env python
# python programa to comunicate with an MCP3008
# Import our SpiDev wrapper and our sleep function
import spidev
from time import sleep

# Establish SPI device on Bus 0,Device 0
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

def getAdc (channel):
              #check valid channel
              if ((channel>7)OR(channel<0)):
                       return -1

              # Preform SPI transaction and store returned bits in 'r'
              r = spi.xfer([1, (8+channel) << 4, 0])

              #Filter data bits from retruned bits
              adcOut = ((r[1]&3) << 8) + r[2]
              
              if ((adcOut > 778)OR(adcOut < 386)):
                      print("Out of range error", adcOut)
                       
              else:
                       percent = ((778 - adcOut) / 392)*100

                       #print out 0-1023 value and percentage
                       print("ADC Output: {:3} Percentage: {:.1f} %".format (adc,percent ))
                          

while True:
              getAdc(0)
              sleep (1)
              