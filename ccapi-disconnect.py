#!/usr/bin/python3

# This script will perform the initial connection Canon mirrorless/SLR camera
# that supports Canon's camera control API (CCAPI)
# this initial connection is needed in order for the camera
# to accept additional commands.

import requests
import json
import config

def disconnect():

    endpoint = '/ccapi/ver'+str(config.VERSION)+'/functions/wificonnection'

    param = json.dumps({'action': 'disconnect'})

    response = requests.post(config.BASE_URL+endpoint)