
# coding: utf-8

# In[1]:


class Card:
    numberOfCards = 0
    def __init__(self, rank=None, suit=None):
        if not suit or rank == None:
            raise ValueError("error: suit and rank are needed")
        self._suit = suit
        # possible ranks [0,1,2,3,4,5,6,7,8,9, 10,11,12]
        #  ---> repr     [A,2,3,4,5,6,7,8,9,10, J, Q, K]
        self._rank = rank
        self._rank_names = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        Card.numberOfCards += 1
    def __del__(self):
        Card.numberOfCards -= 1
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def _less_than(self, c1, c2):
        rc1 = c1.get_rank()
        rc2 = c2.get_rank()
        # zero is the Ace
        if rc1 == 0:
            print("is an ace")
            rc1 = 13
        if rc2 == 0:
            rc2 = 13
#         if type(rc1) == str and rc1 in "JQKA":
#             rc1 = 9 + "JQKA".index(rc1)
#         if type(rc2) == str and rc2 in "JQKA":
#             rc2 = 9 + "JQKA".index(rc2)
        return rc1 < rc2
    def __repr__(self):
        return str(self._suit) + str(self._rank_names[self._rank])
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
    def __neg__(self):
        r = self._rank
        if r == 0:
            r = 13
        return -r


# In[2]:


class Hand:
    def __init__(self, cards):
        self.cards = cards


# In[3]:


class PokerHand(Hand):
    def __gt__(self, other_hand):
        if len(self.cards) != len(other_hand.cards):
            raise ValueError("Hands need to have same number of cards!")
        if max(self.cards) > max(other_hand.cards):
            return True
        elif max(self.cards) == max(other_hand.cards):
            h1 = sorted(self.cards)
            h2 = sorted(other_hand.cards)
            h1_max = False
            for card1, card2 in zip(h1, h2):
                if card1 > card2:
                    h1_max = True
                    break
                elif card1 == card2:
                    continue
                else: # card1 < card2:
                    h1_max = False
                    break
            return h1_max
        else:
            return False
    def __eq__(self, other_hand):
        pass


# In[4]:


class Deck:
    """standard French Deck (52 cards)"""
    def __init__(self):
        self.suits = ["H" , "S" , "D", "C"]
        self.ranks = [x for x in range(0,13)] #["A",2,3,4,5,6,7,8,9,10,"J","C","Q","K"]
        self.cards = [Card(r,s) for s in self.suits for r in self.ranks]


# In[5]:



d = Deck()
print(len(d.cards))
print(d.cards[-5:])


# In[6]:


c1 = Card(3,"H")
c2 = Card(3,"H")
c2 > c1


# In[7]:


c2 == c1


# In[8]:


h1 = PokerHand([Card(0,"H"), Card(10,"H")])
h2= PokerHand([Card(3,"C"), Card(4,"C")])


# In[9]:


h1 > h2


# In[10]:


h2 > h1


# In[11]:


c1.numberOfCards


# In[12]:


sorted(h1.cards,key=lambda x: -x)


# In[13]:


h1.cards[0]._rank


# In[14]:


from random import shuffle
shuffle(d.cards)
print(d.cards)


# In[29]:


# abgeleitet von Card
class FancyCard(Card):
    def __init__(self, rank = None, suit= None):
        super().__init__(rank=rank, suit=suit)
    def __repr__(self):
        spades =   '🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮'
        hearts =   '🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾'
        diamonds = '🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎'
        clubs =    '🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞'
        cards = {'S': spades, 'H': hearts, 'C': clubs, 'D': diamonds}
        return cards[self._suit][self._rank]
    def __del__(self):
        print("bye bye")


# In[30]:


c = FancyCard(rank=0, suit='H')


# In[31]:


c


# In[61]:


class FancyDeck(Deck):
    """fancy French Deck (52 cards)"""
    def __init__(self):
        super().__init__()
        self.cards = [FancyCard(r,s) for s in self.suits for r in self.ranks]


# In[62]:


fd = FancyDeck()


# In[63]:


shuffle(fd.cards)


# In[64]:


print(fd.cards)

