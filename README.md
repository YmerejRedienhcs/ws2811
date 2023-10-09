# ws2811
simple python code for controlling a string of Alitove WS2811 RGB lights

warning: this is crap code

useful link for circuit: https://raspberrypi.stackexchange.com/questions/120494/how-do-i-connect-a-raspberry-pi-to-ws2811-led-lights-through-gpio18-pin

useful link for installing python libraries: https://opensource.com/article/21/1/light-display-raspberry-pi

`sudo apt-get install python3-pip`
Then install the following libraries:

  - rpi_ws281x: `sudo pip3 install rpi_ws281x`
  - Adafruit-circuitpython-neopixel: `sudo pip3 install Adafruit-circuitpython-neopixel`
  - Adafruit-blinka: `sudo pip3 install Adafruit-blinka`

note not all node versions work on RPi Zero.

other good stuff https://github.com/Ziagl/raspberry-pi-ws2811

# SERVICE

References:  

https://www.raspberrypi.com/documentation/computers/using_linux.html#creating-a-service
Creating a service in https://domoticproject.com/creating-raspberry-pi-service/
`man 5 systemd.service`
https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files

The file xmastreelights.service defines the service.

To install the service:
```
  sudo cp xmastreelights.service /etc/systemd/system/
  sudo systemctl daemon-reload
```

To start the service: 

  `sudo systemctl start xmastreelights.service`

To stop the service: 

  `sudo systemctl stop xmastreelights.service`

To restart the service: 

  `sudo systemctl restart xmastreelights.service`

Add the following to root's crontab with `sudo crontab -e`:
```
# Restart the Christmas tree light service every five minutes.
# Each time it restarts, it chooses a different program to run.
*/5 * * * * systemctl restart xmastreelights.service
```

test change to enable creation of a PR to play with

