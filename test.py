import requests
import time

while True:
    # Make request
    response = requests.get("http://vps1.nickforall.nl:6123/packages")
    data = response.json()

    # print(data['packages'])

    for i in data['packages']:
        # Print the status code of the response.
        print("-----------------------------------")
        print("package: "+i['_id'])
        print("name: "+i['name'])
        print("status: "+i['status'])
        print("unlocked: "+str(i['unlocked']))
        if i['unlocked']:
            print("This package is unlocked (by user) - Open the locker")
        else:
            print("This package is stil locked - Do nothing")
        print("-----------------------------------")
        print("")

    print("+++++++++++++++++++++++++++++++++++")
    print("")

    time.sleep(1)