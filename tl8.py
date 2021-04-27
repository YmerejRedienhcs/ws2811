#!/usr/bin/python3
import sys
import board
import neopixel
import time
import random
import asyncio

if len(sys.argv) > 1:
    num_lights = int(sys.argv[1])
else:
    num_lights = 50
print(f'num_lights is {num_lights}')

seg_length = 10

# transform between RGB color and GBR
# goes both ways since it just swaps the first two of the tuple
def t(c):
    return (c[1], c[0], c[2])

black = (0, 0, 0)
white = (255, 255, 255)

def sleep(seconds):
    time.sleep(seconds)

async def slowOn(x):
   c = randomColor(x)
   delay = .020
   for y in range(256):
       #print(f'y is {y}')
       pc = float(y+1) / 256.0
       #print(f'pc is {pc}')
       #c2 = (int(pc * c[0]), int(pc * c[1]), int(pc * c[2]))
       c2 = (pc * c[0], pc * c[1], pc * c[2])
       #print(f'c2 is {c2}')
       await asyncio.sleep(delay * (1-pc))
       pixels[x] = c2

   str[x] = c2


def setLights(str):
  for n in range(len(str)):
    pixels[n] = str[n]

async def blink(n):
    c = str[n]
    str[n] = black
    pixels[n] = black
    await asyncio.sleep(0.5)
    str[n] = c
    pixels[n] = c
    
async def blinks(which):
    count = 0
    while (True):
        await blink(which[count])
        count = (count + 1) % len(which)
        await asyncio.sleep(1)

async def fade(n):
    # c = str[n]
    await slowOn(n)

async def fades(which):
    count = 0
    while (True):
        await fade(which[count])
        count = (count + 1) % len(which)
        await asyncio.sleep(1)
        
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
yellow  = t((255, 255, 000))
white   = t((255, 255, 255))
purple  = t((75, 0, 130))

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

def randomColor(x):
    #return (colors[0])
    r = random.randint(0,5)
    #print (f'r is: {r}')
    return colors[r] # "christmas light colors"

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

setLights(str)

loop = asyncio.get_event_loop()

loop.create_task(blinks([1,3,5]))
loop.create_task(fades([0,2,4]))

loop.run_forever()
loop.close()


for n in range(100):
  r = random.randint(0,len(str)-1)
  slowOn(r)
pixels.fill(black)

delay = 0.04
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
