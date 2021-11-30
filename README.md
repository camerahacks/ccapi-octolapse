# Octoprint Canon Camera Control API Scripts

This is a set of scripts to create Octolapses with a Canon camera that supports the Camera Control API (CCAPI).

You can control your Canon camera wirelessly since CCAPI enabled cameras can be controlled over wifi.

## Canon Camera Control API (CCAPI)

Follow the link below for a list of supported cameras and how to enable CCAPI on your camera.

[CCAPI How To @ DPHacks.com](https://dphacks.com/how-to-canon-camera-control-api-ccapi/)

## Octolapse Setup

Add a new camera in Octolapse config.

Give it a name. Here, I just named it CCAPI.

Set the Camera Type to External Camera - Script

### External Camera Setup - Script

Add the full path to ```ccapi-trigger.py```. In my case it is ```/home/pi/scripts/ccapi-trigger.py```

This is the script that will send a signal to the camera to trip the shutter.

