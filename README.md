# Octoprint Canon Camera Control API Scripts

Although this is a work in progress, the scripts are fully functional.

This is a set of scripts to create Octolapses with a Canon camera that supports the Camera Control API (CCAPI)

You can control your Canon camera wirelessly since CCAPI enabled cameras can be controlled over wifi.

## Canon Camera Control API (CCAPI)

Follow the link below for a list of supported cameras and how to enable CCAPI on your camera.

[CCAPI How To @ DPHacks.com](https://dphacks.com/how-to-canon-camera-control-api-ccapi/)

## Octolapse Setup

Add a new camera in Octolapse config.

Give it a name. Here, I just named it CCAPI.

Set the Camera Type to External Camera - Script

### External Camera Setup - Script

Always add the full path to the scripts below in each one of Octolapse's fields. For example, the full path for ```ccapi-trigger.py``` is ```/home/pi/scripts/ccapi-trigger.py```.

```ccapi-connect.py``` stablishes the first connection with the camera.

```ccapi-trigger.py``` sends a signal to trip the shutter on the camera.

First things first. Set your camera's IP address in ```config.py```. You shouldn't have to change any of the other settings, but they are there if you need it.

```python
# Camera IP Address
IP = '192.168.1.27'

# Camera port. Default is 8080
PORT = '8080'

# Protocol. Default is http
PROTOCOL = 'http'

BASE_URL = PROTOCOL+'://'+IP+':'+PORT

# Turn Auto-focus On/Off during shooting
AF = False
```

## Timelapse Technique

Set the camera to manual exposure and dial in the exposure before starting the timelapse. If the camera is set to any of the automatic exposure modes (Av, Tv, Auto, Etc) the exposure will be ever so lightly different in each frame/picture. This will case the finished timelapse clip to apper to flicker.
