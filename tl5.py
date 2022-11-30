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
seg_length = 100
black = (0, 0, 0)
white = (255, 255, 255)
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

def slowOn(x):
   c = randomColor(x)
   delay = .020
   for y in range(256):
       #print(f'y is {y}')
       pc = float(y+1) / 256.0
       print(f'pc is {pc}')
       #c2 = (int(pc * c[0]), int(pc * c[1]), int(pc * c[2]))
       c2 = (pc * c[0], pc * c[1], pc * c[2])
       #print(f'c2 is {c2}')
       time.sleep(delay * (1-pc))
       pixels[x] = c2
       
#slowOn(2)
#exit()


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
