#!/usr/bin/env python3

import sys
import board
import neopixel
import time
import random
import asyncio
from datetime import date, timedelta

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


def sleep(seconds):
    time.sleep(seconds)


def blend(c1, c2, c2_percent):
    c1_percent = 1.0 - c2_percent
    return (
        c1[0] * c1_percent + c2[0] * c2_percent,
        c1[1] * c1_percent + c2[1] * c2_percent,
        c1[2] * c1_percent + c2[2] * c2_percent,
    )


async def slow_on(x, steps, delay):
    initial_color = str[x]
    while True:
        final_color = randomColor(x)
        if final_color != initial_color:
            break

    for y in range(steps):
        percent = float(y + 1) / float(steps)
        intermediate_color = blend(initial_color, final_color, percent)
        if delay > 0:
            await asyncio.sleep(delay * (1 - percent))
        pixels[x] = intermediate_color
    str[x] = final_color


def set_lights(str):
    for n in range(len(str)):
        pixels[n] = str[n]


# green, red, blue colors translated from rgb
black = t((0, 0, 0))
blue = t((0, 0, 255))
red = t((255, 0, 0))
magenta = t((255, 0, 255))
green = t((0, 255, 0))
cyan = t((0, 255, 255))
yellow = t((195, 195, 0))
white = t((255, 255, 255))
purple = t((75, 0, 130))
darkpurple = t((52, 21, 57))
pink = t((255, 220, 220))
lightblue = t((25, 25, 255))
lightgreen = t((120, 255, 120))
orange = t((255, 87, 51))
rust = t((183, 65, 14))
brown = t((101, 67, 33))
burgundy = t((128, 0, 32))
gold = t((212, 175, 55))
mustard = t((196, 160, 0))
cream = t((245, 235, 220))
olive = t((107, 142, 35))
beige = t((210, 180, 140))
lavender = t((230, 190, 255))
pastelyellow = t((255, 245, 180))
mint = t((180, 255, 200))
robinblue = t((170, 220, 255))
pastelpink = t((255, 200, 220))
silver = t((192, 192, 192))
icyblue = t((180, 225, 255))

# ---------------------------------------------------------------------------
# Edit here
#
# DEFAULT_LEAD_DAYS is used if a holiday does not specify lead_days.
# PALETTES controls the colors used for each holiday.
# HOLIDAYS controls the holiday order, dates, lead time, and palette.
#
# Holiday types:
#   fixed        -> month/day
#   nth_weekday  -> nth weekday in a month (weekday: Monday=0 ... Sunday=6)
#   last_weekday -> last weekday in a month (weekday: Monday=0 ... Sunday=6)
#   easter       -> Gregorian Easter Sunday
# ---------------------------------------------------------------------------

DEFAULT_LEAD_DAYS = 14

PALETTES = {
    'new_years': [
        white,
        gold,
        silver,
        icyblue,
        lightblue,
    ],
    'valentines': [
        white,
        red,
        pink,
        purple,
        red,
        pink,
        magenta,
        pink,
    ],
    'st_patricks': [
        green,
        green,
        lightgreen,
        white,
        orange,
        yellow,
        gold,
    ],
    'easter': [
        white,
        lavender,
        pastelyellow,
        mint,
        robinblue,
        pastelpink,
    ],
    'patriotic': [
        red,
        white,
        blue,
    ],
    'halloween': [
        orange,
        orange,
        orange,
        orange,
        orange,
        white,
        purple,
        darkpurple,
        yellow,
        orange,
        orange,
        orange,
        white,
    ],
    'thanksgiving': [
        orange,
        rust,
        gold,
        mustard,
        burgundy,
        brown,
        olive,
        cream,
        beige,
    ],
    'christmas': [
        white,
        red,
        green,
        blue,
        yellow,
        purple,
        magenta,
        cyan,
        black,
    ],
}

HOLIDAYS = [
    {
        'name': "New Year's Day",
        'type': 'fixed',
        'month': 1,
        'day': 1,
        'lead_days': 6,
        'palette': 'new_years',
    },
    {
        'name': "Valentine's Day",
        'type': 'fixed',
        'month': 2,
        'day': 14,
        'lead_days': 10,
        'palette': 'valentines',
    },
    {
        'name': "St. Patrick's Day",
        'type': 'fixed',
        'month': 3,
        'day': 17,
        'lead_days': 10,
        'palette': 'st_patricks',
    },
    {
        'name': 'Easter',
        'type': 'easter',
        'lead_days': 10,
        'palette': 'easter',
    },
    {
        'name': 'Memorial Day',
        'type': 'last_weekday',
        'month': 5,
        'weekday': 0,
        'lead_days': 10,
        'palette': 'patriotic',
    },
    {
        'name': 'Independence Day',
        'type': 'fixed',
        'month': 7,
        'day': 4,
        'lead_days': 10,
        'palette': 'patriotic',
    },
    {
        'name': 'Halloween',
        'type': 'fixed',
        'month': 10,
        'day': 31,
        'lead_days': 14,
        'palette': 'halloween',
    },
    {
        'name': 'Thanksgiving',
        'type': 'nth_weekday',
        'month': 11,
        'weekday': 3,
        'n': 4,
        'lead_days': 10,
        'palette': 'thanksgiving',
    },
    {
        'name': 'Christmas',
        'type': 'fixed',
        'month': 12,
        'day': 25,
        'lead_days': 18,
        'palette': 'christmas',
    },
]


async def blink(n, time_off):
    c = str[n]
    str[n] = black
    pixels[n] = black
    await asyncio.sleep(time_off)
    str[n] = c
    pixels[n] = c


async def blinks(which, delay_between_blinks, time_off):
    print(f'len(which) is: {len(which)}')
    while True:
        r = random.randint(0, len(which) - 1)
        print(f'blinks: r is: {r}')
        await blink(which[r], time_off=0.25)
        if delay_between_blinks > 0:
            await asyncio.sleep(delay_between_blinks)


async def fade(n):
    await slow_on(n, steps=50, delay=0.04)


async def fades(which, delay):
    while True:
        r = random.randint(0, len(which) - 1)
        print(f'fades: r is: {r}')
        await fade(which[r])
        if delay > 0:
            await asyncio.sleep(delay)


pixels = neopixel.NeoPixel(board.D18, num_lights)
pixels.fill(black)

# Colors must be supplied to pixels as grb colors,
# but I think in rgb.
str = []


def nth_weekday_of_month(year, month, weekday, n):
    d = date(year, month, 1)
    days_until_weekday = (weekday - d.weekday()) % 7
    d += timedelta(days=days_until_weekday)
    d += timedelta(weeks=n - 1)
    return d


def last_weekday_of_month(year, month, weekday):
    if month == 12:
        d = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        d = date(year, month + 1, 1) - timedelta(days=1)
    while d.weekday() != weekday:
        d -= timedelta(days=1)
    return d


def easter_date(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day)


def holiday_date(holiday, year):
    if holiday['type'] == 'fixed':
        return date(year, holiday['month'], holiday['day'])
    if holiday['type'] == 'nth_weekday':
        return nth_weekday_of_month(
            year,
            holiday['month'],
            holiday['weekday'],
            holiday['n'],
        )
    if holiday['type'] == 'last_weekday':
        return last_weekday_of_month(
            year,
            holiday['month'],
            holiday['weekday'],
        )
    if holiday['type'] == 'easter':
        return easter_date(year)
    raise ValueError(f"Unsupported holiday type: {holiday['type']}")


def holiday_lead_days(holiday):
    return holiday.get('lead_days', DEFAULT_LEAD_DAYS)


def active_holiday(today=None):
    if today is None:
        today = date.today()

    schedule = []
    for year in (today.year - 1, today.year, today.year + 1):
        for holiday in HOLIDAYS:
            observed_date = holiday_date(holiday, year)
            lead_days = holiday_lead_days(holiday)
            start_date = observed_date - timedelta(days=lead_days)
            palette_name = holiday['palette']
            schedule.append((
                start_date,
                observed_date,
                lead_days,
                holiday['name'],
                PALETTES[palette_name],
            ))

    schedule.sort(key=lambda x: x[0])

    active = schedule[0]
    for candidate in schedule:
        if candidate[0] <= today:
            active = candidate
        else:
            break

    return active


start_date, holiday_date_value, lead_days_value, holiday_name, colors = active_holiday()
print(
    f"Using {holiday_name} colors "
    f"(starts {start_date}, holiday {holiday_date_value}, lead_days {lead_days_value})"
)


def randomColor(x):
    l = len(colors)
    r = random.randint(0, l - 1)
    print(f'r is: {r}')
    return colors[r]

    # not reached at the moment
    if x % 2 == 0:
        return colors[random.randint(0, 5)]
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


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
for i in range(int(num_lights / 2)):
    l.append(2 * i)
print(f'l for blinks is: {l}')
loop.create_task(blinks(l, delay_between_blinks=0.1, time_off=0.25))

# make task for fades
l = []
for i in range(int(num_lights / 2)):
    l.append(2 * i + 1)
print(l)
loop.create_task(fades(l, delay=0.1))

loop.run_forever()
loop.close()
