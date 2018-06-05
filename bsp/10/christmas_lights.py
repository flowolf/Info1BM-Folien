IS_UPY = False
try:
    import machine, neopixel, network
except:
    pass
else:
    IS_UPY = True

from random import randrange

import time, json, os
try:
    import urequests as requests
except:
    import requests

from settings import DIMM, SLEEP_INTERVAL, READ_INTERVAL, LEDPIN

if IS_UPY:
    np = neopixel.NeoPixel(machine.Pin(LEDPIN),10)
    np.fill((0,0,0))
    np.write()

def show_colors_on_leds(colors):
    """write array of color tuples to leds"""
    if IS_UPY:
        for i in range(10):
            np[i] = colors[i]
        np.write()
    else:
        print(enc_cs)

def running_red_dot(speed=0.5):
    red = (int(240*DIMM),int(10*DIMM),0)
    index = 0
    index2 = 9
    np.fill((0,0,0))
    np[index] = red
    delay = speed/10
    flip = True
    while True:
        if flip:
            index2 -= 1
            if index2 <= 0:
                index = 0
                flip = not flip
            act_index = index2
        else:
            index += 1
            index %= 10
            if index >= 9:
                index2 = 9
                flip = not flip
            act_index = index
        np.fill((0,0,0))
        np[act_index] = red
        np.write()
        time.sleep_ms(int(delay*1000))

def sparcle_rg():
    while True:
        nums = [(randrange(0,100),randrange(0,100),0) for x in range(0,10)]
        np.fill((0,0,0))
        for led in range(0,10):
            np[led] = nums[led]
        np.write()
        #fade_to_black(np)
        time.sleep_ms(100)

def sparcle():
    """sparcle effect"""
    while True:
        np[randrange(0,10)] = (55,25,0)
        np.write()
        fade_to_black(0.8)
        time.sleep_ms(75)

def fade_to_black(step=0.2):
    """fade all leds to black"""
    for index in range(0,10):
        ledr = int(np[index][0]*step) if np[index][0]*step >= 1 else 0
        ledg = int(np[index][1]*step) if np[index][1]*step >= 1 else 0
        ledb = int(np[index][2]*step) if np[index][2]*step >= 1 else 0
        np[index] = (ledr,ledg,ledb)
        print(np[index])
    np.write()

effect = [running_red_dot, sparcle_rg, sparcle]
update_time = 0
while True:
    # run effect
    #effect[0]()
    #effect[1]()
    effect[2]()
