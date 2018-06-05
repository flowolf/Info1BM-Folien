IS_UPY = False
try:
    import machine, neopixel, network
except:
    pass
else:
    IS_UPY = True

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

display_index = 0
def get_and_write_hash_to_pixels():
    r = requests.get("https://blockchain.info/q/latesthash")
    block_hash = r.content.decode()
    r.close()
    enc_cs = get_color_tuples(block_hash)
    if IS_UPY:
        for i in range(10):
            np[i] = enc_cs[i]
        np.write()
    else:
        print(enc_cs)

def get_color_tuples(block_hash):
    colors = [block_hash[i*6+4:i*6+(4+6)] for i in range(10)]
    return [(int(int(c[:2],16)*DIMM),int(int(c[2:4],16)*DIMM),int(int(c[4:6],16)*DIMM)) for c in colors]

def show_hash_on_leds(block_hash):
    print(block_hash)
    enc_cs = get_color_tuples(block_hash)
    if IS_UPY:
        for i in range(10):
            np[i] = enc_cs[i]
        np.write()
    else:
        print(enc_cs)

def get_last_hash():
    r = requests.get("https://blockchain.info/q/latesthash")
    block_hash = r.content.decode()
    r.close()
    return block_hash

def save_file():
    with open(myfile,"w") as f:
        data = {"last10": last10, "index": index}
        f.write(json.dumps(data))

def save_new_hash(block_hash):
    global last10, index
    if block_hash in last10:
        return
    last10[index] = block_hash
    save_file()
    index += 1
    index %= 10

def change_hash_on_leds():
    global display_index
    display_index += 1
    display_index %= 10
    while last10[display_index] == None:
        print(display_index)
        display_index += 1
        display_index %= 10
    show_hash_on_leds(last10[display_index])

def dimm_hash_on_leds():
    global display_index
    oldindex = display_index
    display_index += 1
    display_index %= 10
    while last10[display_index] == None:
        print(display_index)
        display_index += 1
        display_index %= 10
    dimm_over(get_color_tuples(last10[oldindex]), get_color_tuples(last10[display_index]))
    #show_hash_on_leds(last10[display_index])

def show_colors_on_leds(colors):
    """write array of color tuples to leds"""
    if IS_UPY:
        for i in range(10):
            np[i] = colors[i]
        np.write()
    else:
        print(enc_cs)

def dimm_over(old, new, seconds=0.15):
    """calculate dimm effect and display it"""
    # get color diffs
    STEPS = 10
    diffs = []
    for colors in zip(old,new):
        diffr = (colors[1][0] - colors[0][0])
        diffg = (colors[1][1] - colors[0][1])
        diffb = (colors[1][2] - colors[0][2])
        diffs.append((diffr,diffg,diffb))
    # get color values in steps
    frames = []
    for f in range(1,STEPS):
        colors = []
        for index in range(0,10):
            colors.append((round((old[index][0]+diffs[index][0]/STEPS*f)),
                           round((old[index][1]+diffs[index][1]/STEPS*f)),
                           round((old[index][2]+diffs[index][2]/STEPS*f)),
                         ))
        frames.append(colors)
        print(colors)
    frames.append(new)
    # put color values on leds in small time interval
    for colors in frames:
        show_colors_on_leds(colors)
        time.sleep_ms(int(seconds*1000/STEPS))


update_time = 0
while True:
    # check for new block every 2 minutes
    if update_time == 0 or update_time + READ_INTERVAL*1000 < time.ticks_ms():
        update_time = time.ticks_ms()
        # get_and_write_hash_to_pixels()
        bh = get_last_hash()
        save_new_hash(bh)
    print("index: " + str(display_index))
    #dimm_hash_on_leds()
    change_hash_on_leds()
    time.sleep(SLEEP_INTERVAL)
