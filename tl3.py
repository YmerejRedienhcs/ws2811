#!/usr/bin/python3
import sys
import board
import neopixel
import time
import random
if len(sys.argv) > 1:
    num_lights = int(sys.argv[1])
else:
    num_lights = 50
print(f'num_lights is {num_lights}')
seg_length = 15
black = (0, 0, 0)
# program 50 lights with the default brightness 1.0, and autoWrite true
pixels = neopixel.NeoPixel(board.D18, num_lights)
# light 20 bright green
#pixels[19] = (0,255,0)
# light all pixels red
#pixels.fill((255,0,0))
# turn off neopixels
pixels.fill(black)
colors = [
    (000, 000, 000),
    (255, 000, 000),
    (000, 255, 000),
    (000, 000, 255),
    (000, 255, 255),
    (255, 000, 255),
    (255, 255, 000),
    (255, 255, 255)]
def randomColor(x):
    if (x % 2 == 0):
        return colors[random.randint(4,6)]
        #return black
    # return (random.randint(0,127),random.randint(0,127),random.randint(0,127))
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # return colors[random.randint(4,6)]

#for x in range(1000):
#    pixels.fill((255,0,0))
#    pixels.fill((0,255,0))

delay = 0.035
while True:
    for x in range(num_lights+seg_length):
        # print(f'setting light {x} to a color')
        if (x < num_lights):
            pixels[x] = randomColor(x)
        # print(f'x is {x}')
        if ((x >= num_lights) or (x >= seg_length)):
            # print(f'setting light {x-seg_length} to black')
            pixels[x-seg_length] = black
        
        time.sleep(delay)
    
    time.sleep(1)
    pixels.fill((0,0,0))
