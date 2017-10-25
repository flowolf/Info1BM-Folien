# coding: utf-8
int("0b100")
int("0b100",0)
bin(int("0b100",0))
ip_parts=[]
normal_ip = "192.168.5.3"
normal_ip.split(".")
get_ipython().run_line_magic('pinfo', 'normal_ip.split')
normal_ip.split(".", 1)
normal_ip.split(".")
parts = normal_ip.split(".")
parts
ip_parts[0] = int(parts[0])
ip_parts.append( int(parts[0]))
liste = []
liste[0]
ip_parts.append( int(parts[1]))
ip_parts.append( int(parts[2]))
ip_parts.append( int(parts[3]))
ip_parts
liste = [None]*4
liste
liste[0]
bin(255)
bin(255 << 24)
bin((255 << 24) >> 24)
def ip_to_int(ip):
    '''converts classic IP representation to int IP'''
    ip_parts = []
    for element in ip.split('.'):
      ip_parts.append( int(element) )
    int_ip = ip_parts[0] << 24
    int_ip += ip_parts[1] << 16
    int_ip += ip_parts[2] << 8
    int_ip += ip_parts[3]
    return int_ip
ip_to_int("192.168.5.3")
ip = ip_to_int("192.168.5.3")
def convert_ip(ip):
    '''converts an int IP to classic IP `WWW.XXX.YYY.ZZZ`'''
    classic_ip = [None]*4
    classic_ip[0] = (ip & (255 << 24)) >> 24
    classic_ip[1] = (ip & (255 << 16)) >> 16
    classic_ip[2] = (ip & (255 << 8)) >> 8
    classic_ip[3] = (ip & (255))
    str_ip = []
    for element in classic_ip:
      str_ip.append( str(element) )
    return ".".join(str_ip)
ip
convert_ip(ip)
normal_ip
get_ipython().run_line_magic('pinfo', 'normal_ip.join')
get_ipython().set_next_input('".".join');get_ipython().run_line_magic('pinfo', 'join')

def device_number(ip, sub=subnet_24):
    '''returns address of device on the subnet'''
    return ((ip & sub) ^ ip)
subnet_24=ip_to_int("255.255.255.0")
def device_number(ip, sub=subnet_24):
    '''returns address of device on the subnet'''
    return ((ip & sub) ^ ip)
ip
normal_ip
device_number(ip)
convert_ip(ip)
normal_ip = "192.168.10.10"
ip = ip_to_int(normal_ip)
ip
device_number(ip)
(9,0)
a = (9,0)
a[0]
a[0] = 10
b = [9,0]
b[0]
b[0] = 10
b
s = "This is a test string"
s[0]
s[8]
s[-7]
s[1:6]
s[1:12:2]
s[-4]
s[-4:]
s[4:]
s[-44:]
s[-4:]
s[:4]
s[:-4]
s[-11::3]
s[:-5:]
s[::-1]
s[:-5:-1]
s[-16::-1]
s[-16]
s
s[:-5:-1]
s[-16::-1]
s[-5:-12:-2]
my_list = [0,1,2,3,4,5,6,7]
for el in my_list:
    el**2
    
for el in my_list:
    print(el**2)
    
    
[x**2 for x in my_list]
squares = [x**2 for x in my_list]
squares
my_list = [0,1,2,3,4,5,6,7]
[x**2 for x in my_list if x%2 == 0]
my_list1= ["a","b","c"]
my_list2 = ["d","e","f"]
[(a,b) for a in my_list1 for b in _my_list2]
[(a,b) for a in my_list1 for b in my_list2]
my_list3 = ["g","h","i"]
[(a,b,c) for a in my_list1 for b in my_list2 for c in my_list3]
suits = ["H", "S", "C", "D"]
ranks = list(range(2,11))
ranks
ranks.append("J")
ranks.append("Q")
ranks.append("K")
ranks.append("A")
ranks
possible_cards = [(r,s) for s in suits for r in ranks]
possible_cards
import random
deck = possible_cards[:]
# Vorsicht beim Kopieren von Listen
a = [1,2,3,4]
b = a
b
b[1] = 3
a
b = a[:]
b[1] = 2
b
a
deck
len(deck)
possible_cards
# mischen
random.shuffle(deck)
deck
# komisch geben
player1 = deck[0:2]
deck = deck[2:]
len(deck)
player2 = deck[0:2]
deck = deck[2:]
len(deck)
# flop
table = deck[0:3]
deck = deck[3:]
len(deck)
table
player1
# burn
_ = deck[0]
deck = deck[1:]
# turn
table += [deck[0]] 
del deck[0]
len(deck)
table
# burn
del deck[0]
# river
table += [deck[0]]
del deck[0]
table
player1
player2
deck += player1
deck += player2
deck += table
len(deck)
_
deck += _
possible_cards.sort()
possible_cards = sorted(possible_cards)
def sq(x):
    return x**2
lambda x: x**2
sq2 = lambda x: x**2
sq2(3)
sq(3)
get_ipython().run_line_magic('pinfo', 'sorted')
s
get_ipython().run_line_magic('pinfo', 's.sort')
a 
a.sort()
get_ipython().run_line_magic('pinfo', 'a.sort')
get_ipython().run_line_magic('pinfo', 'sorted')
a = list(range(0,100))
a
a.sort()
a
random.shuffle(a)
a
sorted(a)
a
sorted(a)
def mysort(x):
    return -x
sorted(a, key=mysort)
sorted(a, key=lambda x: -x)
possible_cards
deck
len(deck)
del deck[50:]
deck
len(deck)
deck += [('K','H')]
deck
len(deck)
sorted(deck,key=lambda (x,y): y)
deck
sorted(deck, key=lambda x,y: y)
sorted(deck, key=lambda x: x[1])
sorted(deck, key=lambda x: x[0])
(lambda x: x**2)(3)
sq = lambda x: x**2
sq(3)
a
a.sort(key=lambda x: -x)
a
random.shuffle(a)
a
sorted(a, key=lambda x: -x)
a
# B-Sprache Einzeiler
s = "Das ist ein Test String"
"".join([(lambda x: x if x not in "aeiouAEIOU" else x+"b"+x.lower())(l) for l in s])
s = "Alle Kinder sind da" 
"".join([(lambda x: x if x not in "aeiouAEIOU" else x+"b"+x.lower())(l) for l in s])
get_ipython().run_line_magic('save', 'live ~0/')
