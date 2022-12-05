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
print(f'num_lights is {num_lights}')
seg_length = 100
black = (0, 0, 0)
white = (255, 255, 255)

def sleep(seconds):
    time.sleep(seconds)

# program 50 lights with the default brightness 1.0, and autoWrite true
#pixels = neopixel.NeoPixel(board.D18, num_lights)

pixels = neopixel.NeoPixel(board.D18, 250, pixel_order=neopixel.RGBW)
#pixels[0] = (255, 0, 0, 0)

#pixels.fill(black)
#print('red')
#pixels[0] = (255, 0, 0)
#sleep(1)
#print('green')
#pixels[0] = (0, 255, 0)
#sleep(1)
#print('blue')
#pixels[0] = (0, 0, 255)
#sleep(1)
#pixels.fill(black)

# light 20 bright green
#pixels[19] = (0,255,0)
# light all pixels red
#pixels.fill((255,0,0))
# turn off neopixels
pixels.fill(black)
# green, red, blue
# red, green, blue
#colors = [
#    (  0,   0,   0), # black
#    (  0,   0, 255), # blue
#    (  0, 255,   0), # green
#    (  0, 255, 255), # cyan
#    (255,   0,   0), # red
#    (255,   0, 255), # magenta
#    (255, 255,   0), # yellow
#    (255, 255, 255)] # white

colors = [
    (200, 200, 200), # white
    (255,   0,   0), # red
    (  0, 255,   0), # green
    (  0,   0, 255), # blue
    (255, 200,   0), # yellow
    ( 75,   0, 130),   # purple (dark magenta)
    (255,   0, 255), # magenta
    (  0, 255, 255), # cyan
    (  0,   0,   0)] # black
def randomColor(x):
    return (colors[0])
#    r = random.randint(0,5)
#    print (f'r is: {r}')
#    return colors[r] # "christmas light colors"
#    if (x % 2 == 0):
#        return colors[random.randint(0,5)]
#    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#for x in range(1000):
#    pixels.fill(randomColor(x))
#    sleep(.010)

delay = 0.025
while True:
    for x in range(num_lights+seg_length):
        # print(f'setting light {x} to a color')
        if (x < num_lights):
            pixels[x] = randomColor(x)
        # print(f'x is {x}')
        if ((x >= num_lights) or (x >= seg_length)):
            # print(f'setting light {x-seg_length} to black')
            pixels[x-seg_length] = black
        
        sleep(delay)
    
    sleep(1)
    pixels.fill((0,0,0))
