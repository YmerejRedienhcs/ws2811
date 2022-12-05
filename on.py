#!/usr/bin/env python3
import sys
import board
import neopixel
import time
import random

if len(sys.argv) > 1:
    num_lights = int(sys.argv[1])
else:
    num_lights = 50

white = (180,255,180)
# program the number of  lights with the default brightness 1.0, and autoWrite true
pixels = neopixel.NeoPixel(board.D18, num_lights)
pixels.fill((255,255,255))
#pixels.fill(white)
