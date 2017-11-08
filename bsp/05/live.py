# coding: utf-8
my_list = [1,2,3,4,5,6,7,8]
from random import shuffle
shuffle(my_list)
my_list
sorted(my_list)
my_list
my_list.sort()
my_list
shuffle(my_list)
sorted(my_list, lambda x: -x)
sorted(my_list,key=lambda x: -x)
class Rectangle:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        print("rectangle")
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getArea(self):
        return self._x * self._y
r = Rectangle(4,6)
type(y)
type(r)
r.getX()
r.getY()
r._x
r.getArea()
class Square(Rectangle):
    pass
s = Square(7,1)
class Square(Rectangle):
    def __init__(self,x):
        self._x = x
        self._y = x
        print("square")
    def getY(self):
        print("there is no y")
s = Square(7)
s.getArea()
class Cuboid(Rectangle):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self._z = z
    def getVolume(self):
        return self.getArea()*self._z
    
cd = Cuboid(1,2,3)
cd.getVolume()
cd.getArea()
class Cube(Cuboid):
    def __init__(self, x):
        super().__init__(x,x,x)
        
c = Cube(3)
c.getVolume()





class Card:
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        self._rank = rank
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        if type(rc1) == str and rc1 in "JQKA":
            rc1 = 10 + "JQKA".index(rc1)
        if type(rc2) == str and rc2 in "JQKA":
            rc2 = 10 + "JQKA".index(rc2)
        return rc1 < rc2
    
class Deck:
    def __init__(self):
        self.suits = [ "H", "S", "C", "D" ]
        self.ranks = [ "A", 2, 3,4 ,5,6 ,7, 8,9,10,
                       "J","Q","K" ]
        self.cards = [Card(rank=r,suit=s) for r in self.ranks 
                       for s in self.suits]
                   
d = Deck()
d.cards
d.cards[0].rank
d.cards[0]._rank
d.cards[0]._suit
d.cards
class Card:
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        self._rank = rank
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        if type(rc1) == str and rc1 in "JQKA":
            rc1 = 10 + "JQKA".index(rc1)
        if type(rc2) == str and rc2 in "JQKA":
            rc2 = 10 + "JQKA".index(rc2)
        return rc1 < rc2
    def __repr__(self):
        return str(self._suit) + str(self._rank)
    
d = Deck()
d.cards
d.cards[3]
d.cards[15]
Card._less_than(d.cards[3],d.cards[15])
def less_than(c1, c2):
    rc1 = c1.get_rank()
    rc2 = c2.get_rank()
    if type(rc1) == str and rc1 in "JQKA":
        rc1 = 10 + "JQKA".index(rc1)
    if type(rc2) == str and rc2 in "JQKA":
        rc2 = 10 + "JQKA".index(rc2)
    return rc1 < rc2
less_than(d.cards[2],d.cards[15])
less_than(d.cards[15],d.cards[2])
class Card:
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        self._rank = rank
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        if type(rc1) == str and rc1 in "JQKA":
            rc1 = 10 + "JQKA".index(rc1)
        if type(rc2) == str and rc2 in "JQKA":
            rc2 = 10 + "JQKA".index(rc2)
        return rc1 < rc2
    def __repr__(self):
        return str(self._suit) + str(self._rank)
    def __lt__(self, c2):
        return self._less_than(self,c2)
    
d.cards[2] < d.cards[15]
d = Deck()
d.cards[2] < d.cards[15]
class Card:
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        self._rank = rank
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        if type(rc1) == str and rc1 in "JQKA":
            rc1 = 10 + "JQKA".index(rc1)
        if type(rc2) == str and rc2 in "JQKA":
            rc2 = 10 + "JQKA".index(rc2)
        return rc1 < rc2
    def __repr__(self):
        return str(self._suit) + str(self._rank)
    def __lt__(self, c2):
        return self._less_than(self,c2)
    def __gt__(self, c2):
        return self._less_than(c2, self)
    
d = Deck()
d.cards[2] > d.cards[15]
class Card:
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        self._rank = rank
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        if type(rc1) == str and rc1 in "JQKA":
            rc1 = 10 + "JQKA".index(rc1)
        if type(rc2) == str and rc2 in "JQKA":
            rc2 = 10 + "JQKA".index(rc2)
        return rc1 < rc2
    def __repr__(self):
        return str(self._suit) + str(self._rank)
    def __lt__(self, c2):
        return self._less_than(self,c2)
    def __gt__(self, c2):
        return self._less_than(c2, self)
    def __eq__(self, c2):
        return self._rank == c2.get_rank()
    
d = Deck()
d.cards[2] == d.cards[15]
d.cards[2] == d.cards[1]
class Card:
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        self._rank = rank
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        if type(rc1) == str and rc1 in "JQKA":
            rc1 = 10 + "JQKA".index(rc1)
        if type(rc2) == str and rc2 in "JQKA":
            rc2 = 10 + "JQKA".index(rc2)
        return rc1 < rc2
    def __repr__(self):
        return str(self._suit) + str(self._rank)
    def __lt__(self, c2):
        return self._less_than(self,c2)
    def __gt__(self, c2):
        return self._less_than(c2, self)
    def __eq__(self, c2):
        return self._rank == c2.get_rank()
    def __ne__(self, c2):
        return self._rank != c2.get_rank()
    
d = Deck()
d.cards[2] != d.cards[1]
d.cards[2] != 12
class Card:
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        self._rank = rank
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        if type(rc1) == str and rc1 in "JQKA":
            rc1 = 10 + "JQKA".index(rc1)
        if type(rc2) == str and rc2 in "JQKA":
            rc2 = 10 + "JQKA".index(rc2)
        return rc1 < rc2
    def __repr__(self):
        return str(self._suit) + str(self._rank)
    def __lt__(self, c2):
        return self._less_than(self,c2)
    def __gt__(self, c2):
        return self._less_than(c2, self)
    def __eq__(self, c2):
        return self._rank == c2.get_rank()
    def __ne__(self, c2):
        return self._rank != c2.get_rank()
    def __mod__(self, c2)::
class Card:
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        self._rank = rank
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        if type(rc1) == str and rc1 in "JQKA":
            rc1 = 10 + "JQKA".index(rc1)
        if type(rc2) == str and rc2 in "JQKA":
            rc2 = 10 + "JQKA".index(rc2)
        return rc1 < rc2
    def __repr__(self):
        return str(self._suit) + str(self._rank)
    def __lt__(self, c2):
        return self._less_than(self,c2)
    def __gt__(self, c2):
        return self._less_than(c2, self)
    def __eq__(self, c2):
        return self._rank == c2.get_rank()
    def __ne__(self, c2):
        return self._rank != c2.get_rank()
    def __mod__(self, c2):
        return self._suit == c2.get_suit()
    
d = Deck()
d.cards[2] % d.cards[1]
d.cards[2] % d.cards[6]
class Hand():
    def __init__(self, cards):
        self.cards = cards
        
class Hand():
    """ basic class to represent a Hand in a card game"""
    def __init__(self, cards):
        self.cards = cards
        
get_ipython().run_line_magic('pinfo', 'Hand')
class PokerHand(Hand):
    def __gt__(self, other_hand):
        if len(self.cards) != len(other_hand.cards):
            raise ValueError("error: hands need to have same amount of cards")
        if max(self.cards) > max(other_hand.cards):
            return True
        elif max(self.cards) == max(other_hand.cards):
            h1 = sorted(self.cards)
            h2 = sorted(other_hand.cards)
            h1_max = False
            for card1, card2 in zip(h1,h2):
                if card1 > card2:
                    h1_max = True
                    break
                elif card1 == card2:
                    continue
                else: # card2 > card1
                    h1_max = False
                    break
            return h1_max
        else:
            return False
d.cards
h1 = PokerHand([Card("A",2)])
h1
h1.cards
h1 = PokerHand([Card(2,"A")])
h1.cards
h1 = PokerHand([Card(2,"H")])
h1.cards
h1 = PokerHand([Card(2,"H"),Card(5,"C"),Card(7,"S")])
h1.cards
sorted(h1.cards)
class PokerHand(Hand):
    def __gt__(self, other_hand):
        if len(self.cards) != len(other_hand.cards):
            raise ValueError("error: hands need to have same amount of cards")
        if max(self.cards) > max(other_hand.cards):
            return True
        elif max(self.cards) == max(other_hand.cards):
            h1 = sorted(self.cards,key=lambda x: -x)
            h2 = sorted(other_hand.cards,key=lambda x: -x)
            h1_max = False
            for card1, card2 in zip(h1,h2):
                if card1 > card2:
                    h1_max = True
                    break
                elif card1 == card2:
                    continue
                else: # card2 > card1
                    h1_max = False
                    break
            return h1_max
        else:
            return False
h1 = PokerHand([Card(2,"H"),Card(5,"C"),Card(7,"S")])
sorted(h1.cards)
class PokerHand(Hand):
    def __gt__(self, other_hand):
        if len(self.cards) != len(other_hand.cards):
            raise ValueError("error: hands need to have same amount of cards")
        if max(self.cards) > max(other_hand.cards):
            return True
        elif max(self.cards) == max(other_hand.cards):
            h1 = sorted(self.cards,key=lambda x: -x)
            h2 = sorted(other_hand.cards,key=lambda x: -x)
            h1_max = False
            for card1, card2 in zip(h1,h2):
                if card1 > card2:
                    h1_max = True
                    break
                elif card1 == card2:
                    continue
                else: # card2 > card1
                    h1_max = False
                    break
            return h1_max
        else:
            return False
    def __lt__(self, other_hand):
        return self.__gt__(other_hand, self)
    
h1 = PokerHand([Card(2,"H"),Card(5,"C"),Card(7,"S")])
sorted(h1.cards)
class PokerHand(Hand):
    def __gt__(self, other_hand):
        if len(self.cards) != len(other_hand.cards):
            raise ValueError("error: hands need to have same amount of cards")
        if max(self.cards) > max(other_hand.cards):
            return True
        elif max(self.cards) == max(other_hand.cards):
            h1 = sorted(self.cards,key=lambda x: -x)
            h2 = sorted(other_hand.cards,key=lambda x: -x)
            h1_max = False
            for card1, card2 in zip(h1,h2):
                if card1 > card2:
                    h1_max = True
                    break
                elif card1 == card2:
                    continue
                else: # card2 > card1
                    h1_max = False
                    break
            return h1_max
        else:
            return False
    def __lt__(self, other_hand):
        return self.__gt__(other_hand, self)
    
class Card:
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        self._rank = rank
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        if type(rc1) == str and rc1 in "JQKA":
            rc1 = 10 + "JQKA".index(rc1)
        if type(rc2) == str and rc2 in "JQKA":
            rc2 = 10 + "JQKA".index(rc2)
        return rc1 < rc2
    def __repr__(self):
        return str(self._suit) + str(self._rank)
    def __lt__(self, c2):
        return self._less_than(self,c2)
    def __gt__(self, c2):
        return self._less_than(c2, self)
    def __eq__(self, c2):
        return self._rank == c2.get_rank()
    def __ne__(self, c2):
        return self._rank != c2.get_rank()
    def __mod__(self, c2):
        return self._suit == c2.get_suit()
    
c1 = Card(2,"H")
c2 = Card(5,"C")
c2._rank
c2 < c1
c2 > c1
a = [c1,c2]
a
c3 = Card(3,"H")
a.append(c3)
a
sorted(a
)
sorted(a,key=lambda x: -x)
# missing operator for -Card
# follows next time
