#!/usr/bin/python
#
# When writing a file, it follows the sequence of open, write, close
#
#

import time
import board
import adafruit_dht

#comment and uncomment the lines below depending on your sensor
#sensor = Adafruit_DHT.DHT11
sensor = adafruit_dht.DHT22(board.D4, use_pulseio=False)
#sensor = Adafruit_DHT.AM2302

#DISABLED
#DHT pin connects to GPIO 4
#sensor_pin = 4

#create a variable to control the while loop
running = True

#new sensor_txt01.txt file created with header
log_file = open("sensor_txt01.txt", "w")
log_file.write("time, date, temperature (C),temperature (F), humidity\n")

#loop forever
while running:

    try:
        #read the humidity and temperature
        humidity = sensor.humidity
        temperature = sensor.temperature

		#humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

        #uncomment the line below to convert to Fahrenheit
        temperature_f = temperature * 9/5.0 + 32

        #sometimes you won't get a reading and
        #the results will be null
        #the next statement guarantees that
        #it only saves valid readings
        #if humidity is not None and temperature is not None:

        #print temperature and humidity
        print("Temperature = " + str(temperature) +","+ "Temperature Fahrenheit = " + str(temperature_f) +"," + "Humidity = " + str(humidity))
        #save time, date, temperature in Celsius, temperature in Fahrenheit and humidity in .txt file
        #log_file.write(time.strftime("%H:%M:%S %d/%m/%Y") + ", " + str(temperature) + ", "+ str(temperature_f)+"," + str(humidity) + "\n")
        log_file.write(time.strftime("%Y-%m-%d %H:%M:%S") + ", " + str(temperature) + ", "+ str(temperature_f)+"," + str(humidity) + "\n")
        time.sleep(1)

    # except RuntimeError as error:
    # # Errors happen fairly often, DHT's are hard to read, just keep going
    # #print(error.args[0])
	   #  time.sleep(2.0)
    # 	continue

    # except Exception as error:
    # 	sensor.exit()
    # 	raise error

    except KeyboardInterrupt:
        print ("Program stopped")
        running = False
        log_file.close()

time.sleep(5.0)








