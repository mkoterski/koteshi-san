#!/usr/bin/python
#
# When writing a file, it follows the sequence of open, write, close
#
#

import time
import os.path
import board
import adafruit_dht

#comment and uncomment the lines below depending on your sensor
#sensor = Adafruit_DHT.DHT11
sensor = adafruit_dht.DHT22(board.D4, use_pulseio=False)
#sensor = Adafruit_DHT.AM2302


#create a variable to control the while loop
running = True

#If sensor_log01.txt does not exist, it will be created. Changing mode from write to append

if os.path.exists("sensor_log01.txt"):
    log_file = open("sensor_log01.txt", "a")
else:
    log_file = open("sensor_log01.txt", "w")
    log_file.write("date, time, temperature (C), humidity\n")

#loop forever
while running:

    try:
        #read the humidity and temperature
        humidity = sensor.humidity
        temperature = sensor.temperature

		#humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

        #print temperature and humidity
        print("Temperature: " + str(temperature) + " °C, " + "Humidity: " + str(humidity) + " %")
        #save date, time, temperature in Celsius, and humidity in sensor_log01.txt file
        log_file.write(time.strftime("%Y-%m-%d,%H:%M:%S") + "," + str(temperature) + "," + str(humidity) + "\n")
        time.sleep(1)

    except RuntimeError as error:
    # In case you are interested in the error message you can uncomment the following line
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

time.sleep(3.0)








