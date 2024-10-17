#!/usr/bin/env python3

# Halloween

import sys
import board
import neopixel
import time
import random
import asyncio

debug = False

if len(sys.argv) > 1:
    num_lights = int(sys.argv[1])
else:
    num_lights = 50
print(f'num_lights is: {num_lights}')

seg_length = 10

# transform between RGB color and GBR
# goes both ways since it just swaps the first two of the tuple
def t(c):
    return (c[1], c[0], c[2])

black = (0, 0, 0)
white = (255, 255, 255)

def sleep(seconds):
    time.sleep(seconds)

def blend(c1, c2, c2_percent):
    c1_percent = 1.0 - c2_percent
    return (c1[0]*c1_percent + c2[0]*c2_percent, 
            c1[1]*c1_percent + c2[1]*c2_percent, 
            c1[2]*c1_percent + c2[2]*c2_percent)

async def slow_on(x, steps, delay):
    # print(f'slow_on: x is {x}')
    # print(f'slow_on: steps is {steps}')
    # print(f'slow_on: delay is {delay}')
    initial_color = str[x]
    # print(f'slow_on: initial_color is {initial_color}')
    while True:
        final_color = randomColor(x)
        # print(f'slow_on: final_color is {final_color}')
        if final_color != initial_color:
            break
    
    for y in range(steps):
        # print(f'slow_on: y is {y}')
        percent = float(y+1) / float(steps)
        # print(f'slow_on: percent is {percent}')
        intermediate_color = blend(initial_color, final_color, percent)
        # print(f'slow_on: intermediate_color is {intermediate_color}')
        if delay > 0:
            await asyncio.sleep(delay * (1-percent))
        pixels[x] = intermediate_color
    str[x] = final_color
    #exit()


def set_lights(str):
  for n in range(len(str)):
    pixels[n] = str[n]

async def blink(n, time_off):
    c = str[n]
    str[n] = black
    pixels[n] = black
    await asyncio.sleep(time_off)
    str[n] = c
    pixels[n] = c
    
async def blinks(which, delay_between_blinks, time_off):
    print(f'len(which) is: {len(which)}')
    while (True):
        r = random.randint(0, len(which) - 1)
        print(f'blinks: r is: {r}')
        await blink(which[r], time_off=0.25)
        if delay_between_blinks > 0:
            await asyncio.sleep(delay_between_blinks)

async def fade(n):
    # c = str[n]
    await slow_on(n, steps=50, delay=0.04)

async def fades(which, delay):
    while (True):
        r = random.randint(0, len(which) - 1)
        print(f'fades: r is: {r}')
        await fade(which[r])
        if (delay > 0):
            await asyncio.sleep(delay)
        
# program 50 lights with the default brightness 1.0, and autoWrite true
#pixels = neopixel.NeoPixel(board.D18, num_lights)

# following did not do what I thought it would
#pixels = neopixel.NeoPixel(board.D18, num_lights, pixel_order=neopixel.RGBW)

pixels = neopixel.NeoPixel(board.D18, num_lights)

# set first LED to green
#pixels[0] = (255, 0, 0, 0)

#pixels.fill(black)
#print('red')
#pixels[0] = t((255, 0, 0))
#sleep(1)
#print('green')
#pixels[0] = t((0, 255, 0))
#sleep(1)
#print('blue')
#pixels[0] = t((0, 0, 255))
#sleep(1)
#pixels.fill(black)

# light 20 bright green
#pixels[19] = t((0,255,0))
# light all pixels red
#pixels.fill(t((255,0,0)))
# turn off neopixels
pixels.fill(black)
# green, red, blue
# red, green, blue

# Colors must be supplied to pixels as grb colors,
# but I think in rgb.

# green, red, blue colors translated from rgb
black   = t((  0,   0,   0))
blue    = t((000, 000, 255))
red     = t((255,   0,   0))
magenta = t((255,   0, 255))
green   = t((  0, 255,   0))
cyan    = t((  0, 255, 255))
yellow  = t((195, 195, 000))
white   = t((255, 255, 255))
purple  = t((75, 0, 130))
darkpurple  = t((52, 21, 57))
pink    = t((255, 220, 220))
lightblue = t((25, 25, 255))
lightgreen = t((120, 255, 120))
# orange = t((255, 165, 0))
orange = t((255, 87, 51))

str = []

#pixels.fill(black)
#print('red')
#pixels[0] = red
#sleep(1)
#print('green')
#pixels[0] = green
#sleep(1)
#print('blue')
#pixels[0] = blue
#sleep(1)
#pixels.fill(black)

colors = [
    white,
    red,
    green,
    blue,
    yellow,
    purple,
    magenta,
    cyan,
    black
]

colors = [
    white,
    red,
    pink,
    purple,
    red,
    pink,
    magenta,
    pink,
    black
]

colors = [
    red,
    white,
    blue,
    red,
    white,
    blue,
    red,
    blue,
    black
]

colors = [
    purple,
    yellow,
    lightblue,
    lightgreen,
    pink
]
colors = [
    lightblue,
    purple,
    lightgreen,
    pink
]

# patriotic colors

colors = [
    red,
    white,
    blue
]

# halloween colors

colors = [
    orange,
    orange,
    orange,
    orange,
    orange,
    white,
    black,
    purple,
    darkpurple,
    yellow,
    orange,
    orange,
    orange,
    white,
    black,
]

def randomColor(x):
    l = len(colors)
    r = random.randint(0,l-1)
    print (f'r is: {r}')
    return colors[r]

    #not reached at the moment
    if (x % 2 == 0):
        return colors[random.randint(0,5)]
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#for x in range(1000):
#    pixels.fill(randomColor(x))
#    sleep(.010)

print(type(str))
for n in range(num_lights):
  print(f'n is: {n}')
  rc = randomColor(n)
  print(f'rc is: {rc}')
  str.append(rc)

set_lights(str)

loop = asyncio.get_event_loop()

# make task for blinks
l = []
for i in range(int(num_lights/2)):
    l.append(2*i)
# loop.create_task(blinks([1,3,5])) # a test one blinking just the 2nd, 4th, and 6th 
print(f'l for blinks is: {l}')
loop.create_task(blinks(l, delay_between_blinks=0.1, time_off=0.25))

# make task for fades
l = []
for i in range(int(num_lights/2)):
    l.append(2*i+1)
#loop.create_task(fades([0,2,4])) # a test one fading just the 1st, 3rd, and 5th 
print(l)
loop.create_task(fades(l, delay=0.1))

loop.run_forever()
loop.close()


#for n in range(100):
#  r = random.randint(0,len(str)-1)
#  slow_on(r)
#pixels.fill(black)

#delay = 0.04
#while True:
#    for x in range(num_lights+seg_length):
#        # print(f'setting light {x} to a color')
#        if (x < num_lights):
#            pixels[x] = randomColor(x)
#        # print(f'x is {x}')
#        if ((x >= num_lights) or (x >= seg_length)):
#            # print(f'setting light {x-seg_length} to black')
#            pixels[x-seg_length] = black
#        sleep(delay)
#    
#    sleep(1)
#    pixels.fill((0,0,0))
