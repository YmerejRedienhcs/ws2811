#!/usr/bin/python3
import sys
import board
import neopixel
import time
import random
num_lights = 150
num_lights = int(sys.argv[1])
white = (255,255,255)
# program 50 lights with the default brightness 1.0, and autoWrite true
pixels = neopixel.NeoPixel(board.D18, num_lights)
pixels.fill((255,255,255))
