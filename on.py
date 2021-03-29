#!/usr/bin/python3
import sys
import board
import neopixel
import time
import random

if len(sys.argv) > 1:
    num_lights = int(sys.argv[1])
else:
    num_lights = 250

white = (255,255,255)
# program the number of  lights with the default brightness 1.0, and autoWrite true
pixels = neopixel.NeoPixel(board.D18, num_lights)
pixels.fill((255,255,255))
