#!/usr/bin/python3

# This cript will trip the shutter on a Canon mirrorless/SLR camera
# that supports Canon's camera control API (CCAPI)

import requests
import json

IP = '192.168.1.27'

PORT = '8080'

PROTOCOL = 'http'

BASE_URL = PROTOCOL+'://'+IP+':'+PORT

AF = False

def shutter():

    endpoint = '/ccapi/ver100/shooting/control/shutterbutton'

    param = json.dumps({'af': AF})

    response = requests.post(BASE_URL+endpoint, data=param)

    print(param)


shutter()