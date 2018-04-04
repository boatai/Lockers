import requests
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

def unlock( safeNumber ):
    if safeNumber == 1:
        GPIO.output(17,GPIO.HIGH)
    elif safeNumber == 2:
        GPIO.output(27,GPIO.HIGH)
    else:
        GPIO.output(22,GPIO.HIGH)
    return

def lock( safeNumber ):
    if safeNumber == 1:
        GPIO.output(17,GPIO.LOW)
    elif safeNumber == 2:
        GPIO.output(27,GPIO.LOW)
    else:
        GPIO.output(22,GPIO.LOW)
    return

while True:
    # Make request
    response = requests.get("http://vps1.nickforall.nl:6123/packages")
    data = response.json()

    # print(data['packages'])

    for idx, i in enumerate(data['packages'], 1):
        # Print the status code of the response.
        print("-----------------------------------")
        print("#"+str(idx))
        print("package: "+i['_id'])
        print("name: "+i['name'])
        print("status: "+i['status'])
        print("unlocked: "+str(i['unlocked']))
        if i['unlocked']:
            print("This package is unlocked (by user) - Open the locker")
            unlock(idx)
        else:
            print("This package is stil locked - Do nothing")
            lock(idx)
        print("-----------------------------------")
        print("")

    print("+++++++++++++++++++++++++++++++++++")
    print("")

#    time.sleep(1)