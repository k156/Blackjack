import random
from functools import reduce

g_deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']
random.shuffle(g_deck)

class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

class Card:
    deck = []
    def __init__(self):
        # self.deck = g_deck
        self.cardlist = []        
        self.numberlist = [] 
        self.cardsum = 0

    def mk_cardlist(self):
        global g_deck
        print("g_deck>>", g_deck)
        self.card = g_deck.pop(0)
        self.cardlist.append( self.card )
        
    
    def mk_numberlist(self):    
        
        self.num = self.card.lstrip(self.card[0])
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        
        elif  self.num == 'a':
            self.num = 11 

        else : self.num = Casting.to_int(self.num)

        self.numberlist.append(self.num)  

    def cardsummation(self):
        for i in self.numberlist:
            self.cardsum += i      
           
      

class Player(Card):
    def __init__(self):
        super().__init__()

        super().mk_cardlist()
        super().mk_numberlist()
        super().cardsummation()
        
        print(self.cardlist)
        
        
         
class Dealer(Card):
    def __init__(self):
        
        super().__init__()
        
        while(self.cardsum < 17):
            super().mk_cardlist()
            super().mk_numberlist()
            self.cardsummation()
            
        print("딜러의 카드리스트>>", self.cardlist)
        print(self.cardsum)

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

<<<<<<< HEAD
class Player(Card):
    def game(self):
        super().__init__()
        super().summation()
        
        print(self.cardlist)
    

        super().__init__()
        super().summation()
        if self.cardsum == 21:   print("승")

        elif self.cardsum > 21:   print("패")

        elif self.cardsum < 21:
            hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.")
            
            if hitorstand == '1':   
                self.num = self.card.lstrip(self.card[0])
                print("p cardsum>>" self.cardsum)
            

            if hitorstand == '2': 
                print("p cardsum>>" self.cardsum)

        

class Dealer(Card):
    def __init__(self):
        
        super().__init__()
        super().summation()

        print("d carsum>>" self.cardsum)

# a.cardlist()

a = Card()
a.summation()


b = Player()
b.game


a = Dealer()
=======
elif a.cardsum > b.cardsum :
    print("패")    
>>>>>>> master
