# ws2811
simple python code for controlling a string of Alitove WS2811 RGB lights

warning: this is crap code

useful link for circuit: https://raspberrypi.stackexchange.com/questions/120494/how-do-i-connect-a-raspberry-pi-to-ws2811-led-lights-through-gpio18-pin

useful link for installing python libraries: https://opensource.com/article/21/1/light-display-raspberry-pi

sudo apt-get install python3-pip
Then install the following libraries:

  - rpi_ws281x: `sudo pip3 install rpi_ws281x`
  - Adafruit-circuitpython-neopixel: `sudo pip3 install Adafruit-circuitpython-neopixel`
  - Adafruit-blinka: `sudo pip3 install Adafruit-blinka`

note not all node versions work on RPi Zero.

other good stuff https://github.com/Ziagl/raspberry-pi-ws2811
