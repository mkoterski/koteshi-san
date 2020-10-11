import time
import datetime
from firebase import firebase
import grovepi

watered = False

def automate():
    #if the time is in between an interval of +- 15 mins, while the moisture level < thresh keep motor running, else turn off motor
    thresh = 30
    global watered
    print("watered?", watered)
    time = datetime.datetime.now().strftime("%H:%M")
    print("current time", time)
    if (((time > "19:45") and (time < "20:40")) or ((time > "3:45") and (time < "4:15"))):
        if not watered:
            while True:
                moisture = grovepi.analogRead(moisture_sensor)
                moisture = 100 - (100*moisture/1023)

                if (moisture > thresh):
                    grovepi.digitalWrite(motor, 0)
                    watered = True
                    break

                else:
                    grovepi.digitalWrite(motor,1)
    else:
        watered = False
        grovepi.digitalWrite(motor,0)

dht_sensor = 4
light_sensor = 0
moisture_sensor = 1
motor = 3

grovepi.pinMode(motor, "OUTPUT")
grovepi.pinMode(dht_sensor, "INPUT")
grovepi.pinMode(light_sensor, "INPUT")
grovepi.pinMode(moisture_sensor, "INPUT")

firebase = firebase.FirebaseApplication('https://koteshi-san.firebaseio.com/', None)

initTime = time.time()

while True:
    motor_state = firebase.get('/iot-garden-monitoring-system', 'motor_state')
    update = firebase.get('/iot-garden-monitoring-system', 'update')
    pi_state = firebase.get('/iot-garden-monitoring-system', 'pi_state')

    print("received data in ", int(time.time() - initTime), "seconds")
    initTime = time.time()

    if (pi_state == str("0")):
        grovepi.digitalWrite(motor,0)
        break
    [temp,humidity] = grovepi.dht(dht_sensor, 0)
    light = grovepi.analogRead(light_sensor)
    moisture = grovepi.analogRead(moisture_sensor)

    light = 100*light/1023
    moisture = 100 - (100*moisture/1023)

    print("temp = ", temp)
    print("humidity = ", humidity)
    print("light = ", light)
    print("moisture = ", moisture)


    if (update == str("1")):
        print("updating db")
        firebase.put('iot-garden-monitoring-system', 'temperature', str(temp))
        firebase.put('iot-garden-monitoring-system', 'humidity', str(humidity))
        firebase.put('iot-garden-monitoring-system', 'light', str(light))
        firebase.put('iot-garden-monitoring-system', 'moisture', str(moisture))
        firebase.put('iot-garden-monitoring-system', 'update', str(0))
        
    if (motor_state == str("1")):
        #turn on motor
        print("motor turned on")
        grovepi.digitalWrite(motor,1)
    elif (motor_state == str("2")):
        #automate
        print("motor automatic control")
        automate()
    else:
        #turn off motor
        print("motor turned off")
        grovepi.digitalWrite(motor,0)
