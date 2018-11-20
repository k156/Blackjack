import random
from functools import reduce

deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']

class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

class Card:
  
    def __init__(self):

        global deck
        self.cardlist = []                 
        self.numberlist = [] 

        random.shuffle(deck)
        self.card = deck.pop()
        self.cardlist.append( self.card )
        
        num = self.card.lstrip(self.card[0])
        
        if num == 'k' or num == 'q' or num == 'j':
            num = 10

        elif num == 'a':
            num = 1    
        
        else : num = Casting.to_int(num)

        self.numberlist.append(num)

        print(self.cardlist)
        print(self.numberlist)
  

    def cardsum(self):

        self.cardsum = reduce(lambda x, y: x + y, self.numberlist)       
              
        print(self.cardsum)


a = Card()
a.cardsum()        