import machine, neopixel, network
import time, json, os
import urequests as requests
from settings import DIMM, SLEEP_INTERVAL, READ_INTERVAL, LEDPIN

np = neopixel.NeoPixel(machine.Pin(LEDPIN),10)
np.fill((0,0,0))
np.write()
##############################################################################
myfile = "last10.json"
index = 7
try:
    with open(myfile,"r") as f:
        raw_data = f.read()
        data = json.loads(raw_data)
        last10 = data['last10']
        index = data['index']
        del data
        del raw_data
except (OSError, TypeError):
    last10 = [  "000000000000000000af11ed56cddd78793d9d7cb42ad4b6f0986634c7690518",
                "000000000000000000786daed0aef5332fc3ac44ee1127525eeb16b1a3b6e0be",
                "00000000000000000014515fffe0f07eb8f1fe89d4d184263cbb5983dc5bfbbc",
                "0000000000000000004961f628037d20ad76dec96d46d0c8dfc90bee3481ef60",
                "00000000000000000005dfa9e6053bec0df032c91c63e4ccb635b5ba0fe9dd26", ]
    last10.extend([None]*5)
    pass # ignore error if file is not here

##############################################################################
display_index = 0
