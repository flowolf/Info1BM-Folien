#!/usr/bin/python3
from time import sleep
from datetime import datetime as dt

def hanoi(ring,stab1="stab1",stab2="stab2",stab3="stab3"):
    if ring > 0:
        hanoi(ring-1,stab1,stab3,stab2)
#        print("bewege "+str(ring)+" von " + stab1 + " nach " + stab3)
        move(ring,stab1,stab3)
        hanoi(ring-1,stab2,stab1,stab3)
        sleep(0.001)

def move(ring,stab_a,stab_b):
    # implement moving of robot here!
    pass

def measure(i):
    now = dt.now()
    hanoi(i)
    then = dt.now()
    return(then-now)

def main():
    for i in range(0,40):
        print("RES " + str(i) + ": " + str(measure(i)))

if __name__ == "__main__":
    main()


# python3 ./hanoi.py # sleep 1 second
#RES 0: 0:00:00.000006
#RES 1: 0:00:01.001042
#RES 2: 0:00:03.003122
#RES 3: 0:00:07.007235
#RES 4: 0:00:15.015516
#RES 5: 0:00:31.031974
#RES 6: 0:01:03.064898
#RES 7: 0:02:07.127407
#RES 8: 0:04:15.259753
#RES 9: 0:08:31.517112
#RES 10: 0:17:04.040307

# python3 hanoi.py # sleep 0.001 second
# RES 0: 0:00:00.000009
# RES 1: 0:00:00.001081
# RES 2: 0:00:00.003230
# RES 3: 0:00:00.007523
# RES 4: 0:00:00.016112
# RES 5: 0:00:00.033318
# RES 6: 0:00:00.067728
# RES 7: 0:00:00.136533
# RES 8: 0:00:00.274157
# RES 9: 0:00:00.546585
# RES 10: 0:00:01.099807
# RES 11: 0:00:02.195859
# RES 12: 0:00:04.390246
# RES 13: 0:00:08.777635
# RES 14: 0:00:17.564701
# RES 15: 0:00:35.186316
# RES 16: 0:01:10.315855
# RES 17: 0:02:20.545321
# RES 18: 0:04:41.143681
# RES 19: 0:09:22.309774
# RES 20: 0:18:44.751571
# RES 21: 0:37:25.260524
# RES 22: 1:14:50.028081
