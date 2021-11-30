#!/usr/bin/python3

# This script will trip the shutter on a Canon mirrorless/SLR camera
# that supports Canon's camera control API (CCAPI)

import requests
import json
import config

def shutter():

    endpoint = '/ccapi/ver100/shooting/control/shutterbutton'

    param = json.dumps({'af': config.AF})

    response = requests.post(config.BASE_URL+endpoint, data=param)

    print(param)

shutter()