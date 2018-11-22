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
        self.num = self.card.lstrip(self.card[0])
    
    
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        
        elif  self.num == 'a':
            self.num = 11

        else: 
            self.num = Casting.to_int(self.num)
            self.numberlist.append(self.num)
            self.cardsummation()

        # print(self.cardlist)
        # print(self.numberlist)
    

    def cardsummation(self):

        self.cardsum = reduce(lambda x, y: x + y, self.numberlist)       
           
      

class Player(Card):
    def __init__(self):
        super().__init__()
        super().cardsummation()

        print('player cardlist>>', self.cardlist)
        
        
         
class Dealer(Card):
    def __init__(self):
        
        super().__init__()
        super().cardsummation()

        while(self.cardsum < 17):
            super().__init__()
            super().cardsummation()
        
        print("딜러 카드리스트>>", self.cardlist)
        print("딜러의 카드 총 합>>>",self.cardsum)

# a.cardlist()
a = Player()
b = Dealer() 

# while(a.cardsum < 21):
    
#     if a.cardsum == 21:   print("승")

#     elif a.cardsum > 21:   print("패")

#     elif a.cardsum < 21:
#         hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.")
        
#         if hitorstand == '1':   
#             continue

#         if hitorstand == '2': 
#             print(a.cardsum)
#             break



# while(b.cardsum < 17)

#     if b.cardsum == 21:   
#         print(b.cardsum)
#         break

#     elif b.cardsum > 21:   
#         print("player 승")



print("승패 결과는???????")
if a.cardsum < b.cardsum :
    print("승")

elif a.cardsum == b.cardsum :
    print("비김")    

elif a.cardsum > b.cardsum :
    print("패")    