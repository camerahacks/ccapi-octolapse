# !/usr/bin/python3

# This cript will perform the initial connection Canon mirrorless/SLR camera
# that supports Canon's camera control API (CCAPI)
# this initial connection is needed in order for the camera
# to accept additional commands.

import requests

IP = '192.168.1.27'

PORT = '8080'

PROTOCOL = 'http'

BASE_URL = PROTOCOL+'://'+IP+':'+PORT

def shutter():

    endpoint = '/ccapi'

    response = requests.get(BASE_URL+endpoint)

shutter()