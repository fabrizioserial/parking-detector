
# Parking Detector

Identify all the available parking spaces with top view camera using Python.


## Installation

### Install Python3 and Pip

[Python3 & PIP Windows Installation](https://phoenixnap.com/kb/how-to-install-python-3-windows)

[Python3 MacOS Installation](https://www.freecodecamp.org/espanol/news/como-instalar-python3-en-mac-b/)

[PIP MacOS Installation](https://www.groovypost.com/howto/install-pip-on-a-mac/#:~:text=To%20use%20the%20get%2Dpip,pip.py%20and%20press%20Enter.)


### Install dependencies

```bash
  pip install -r requirements.txt
```

# Usage
## Identify parking spaces
### Run selection tool
In order to run the script, you must first identify manually all parking spaces, including both ocupied and free ones.

To do so, execute the following command to run the parking space selection tool:

```bash
  python ParkingSpacePicker.py
```
This tool will open a window showing in this case the `resources/parking.png` image.

You should replace `resources/parking.png` with an according top view image of your parking lot.

### Spaces selection
Once you have executed the selection tool, follow these instructions to mark/unmark parking spaces:
+ Left click the left top corner of each parking space
+ Right click inside an existing parking space to delete it 

## Running the script
After marking parking spaces, you are ready to execute the script which will show if the parking spaces are available or occupied.
To do so, run the following command:
```bash
  python main.py
```
This will load the selected video/stream through the line 8:  `cv.VideoCapture('resources/topdownparking.mp4')`. Replace it with your live stream/parking lot video.
A window with all previously marked spaces will show up. If the parking space is free, the rectangle will be red, else, it will be colored green.

Adjust the space-occupation threshold by modifying the default `200` value from `if count < 200:` in line 23.
