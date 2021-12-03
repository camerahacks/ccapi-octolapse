# Octoprint Canon Camera Control API Scripts

Although this is a work in progress, the scripts are fully functional.

This is a set of scripts to create Octolapses with a Canon camera that supports the Camera Control API (CCAPI)

You can control your Canon camera wirelessly since CCAPI enabled cameras can be controlled over wifi.

## Canon Camera Control API (CCAPI)

Follow the link below for a list of supported cameras and how to enable CCAPI on your camera.

[CCAPI How To @ DPHacks.com](https://dphacks.com/how-to-canon-camera-control-api-ccapi/)

Here's a list of compatible cameras (as of December 2021)

| Camera                 | CCAPI v1.1         | CCAPI v1.0         |
|------------------------|--------------------|--------------------|
| EOS M50 Mark II        |                    | :heavy_check_mark: |
| EOS R5                 | :heavy_check_mark: | :heavy_check_mark: |
| EOS R6                 | :heavy_check_mark: | :heavy_check_mark: |
| EOS Rebel T8i          |                    | :heavy_check_mark: |
| EOS 1D X Mark III      | :heavy_check_mark: | :heavy_check_mark: |
| EOS M200               |                    | :heavy_check_mark: |
| EOS M6 Mark II         |                    | :heavy_check_mark: |
| EOS 90D                |                    | :heavy_check_mark: |
| EOS Rebel SL3          |                    | :heavy_check_mark: |
| EOS RP                 |                    | :heavy_check_mark: |
| Powershot SX70 HS      |                    | :heavy_check_mark: |
| PowerShot G5 X Mark II |                    | :heavy_check_mark: |
| PowerShot G7 X Mark III|                    | :heavy_check_mark: |

![Canon EOS RP - Camera Control API](https://i0.wp.com/dphacks.com/wp-content/uploads/2019/04/Canon-CCAPI-EOS-RP_1.jpg?resize=768%2C512&ssl=1 "Canon EOS RP - CCAPI")

## Octolapse Setup

Add a new camera in Octolapse config.

<img src="img\Octolapse_Setup_Step_1.png" width="80%">

<img src="img\Octolapse_Setup_Step_2.png" width="80%">

### Basic Settings

Give it a name and a description. Here, I just named it CCAPI. Do not choose a Profile to Import and make sure to select External Camera - Scrip under the Camera Type section.

<img src="img\Octolapse_Setup_Step_3.png" width="80%">


### External Camera Setup - Script

Always add the full path to the scripts below in each one of Octolapse's fields. For example, the full path for ```ccapi-trigger.py``` is ```/home/pi/scripts/ccapi-trigger.py```.

<img src="img\Octolapse_Setup_Step_4.png" width="80%">


### Custom Camera Scripts

<img src="img\Octolapse_Setup_Step_5.png" width="80%">

```ccapi-connect.py``` Establishes the first connection with the camera.

```ccapi-disconnect.py``` Terminates CCAPI and disconnects the camera from Wi-fi network.

```ccapi-trigger.py``` Sends a signal to trip the shutter on the camera.

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

# Liveview options
LVSIZE = 'small'

DISPLAY = 'off'

# Disconnect camera from Wi-fi after print is complete
DISCONNECT = True
```

## Camera Setup

## Timelapse Technique

Set the camera to manual exposure and dial in the exposure before starting the timelapse. If the camera is set to any of the automatic exposure modes (Av, Tv, Auto, Etc) the exposure will be ever so lightly different in each frame/picture. This will case the finished timelapse clip to apper to flicker.
