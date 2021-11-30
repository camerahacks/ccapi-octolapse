#!/usr/bin/python3

# This script will perform the initial connection Canon mirrorless/SLR camera
# that supports Canon's camera control API (CCAPI)
# this initial connection is needed in order for the camera
# to accept additional commands.

import requests
import config

def connect():

    endpoint = '/ccapi'

    response = requests.get(config.BASE_URL+endpoint)

connect()