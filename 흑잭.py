import random
from functools import reduce

deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']
random.shuffle(deck)
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
        
        self.card = deck.pop()
        self.cardlist.append( self.card )
        
        self.num = self.card.lstrip(self.card[0])
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        
        elif  self.num == 'a':
            self.num = 11

        else : self.num = Casting.to_int(self.num)

        self.numberlist.append(self.num)


    def cardsummation(self):

        self.cardsum = reduce(lambda x, y: x + y, self.numberlist)       


    def gameplay(self):
        self.card = deck.pop()
        self.cardlist.append( self.card )
        self.num = self.card.lstrip(self.card[0])
    
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        
        elif  self.num == 'a':
            self.num = 11

        else : self.num = Casting.to_int(self.num)

        self.numberlist.append(self.num)
        self.cardsummation()  
    

class Player(Card):
    def __init__(self):
        super().__init__()
        super().cardsummation()
        
        while( self.cardsum < 21):
            super().gameplay()
            print("플레이어의 카드>>>", self.cardlist)
            if self.cardsum == 21:
                print(self.cardsum)
                
            elif self.cardsum > 21:
                print(self.cardsum)
                
            elif self.cardsum < 21:
                hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.")

                if hitorstand == '1':
                    continue

                elif hitorstand == '2': 
                    
                    print("플레이어의 카드>>>", self.cardlist)
                    print("플레이어의 카드 총 합>>>",self.cardsum)
                    break
   

        
class Dealer(Card):
    def __init__(self):
        
        super().__init__()
        super().cardsummation()

        while(self.cardsum < 17):
            super().gameplay()

        # print("딜러의 최종 카드>>>", self.cardlist)
        print("딜러의 카드 총 합>>>", self.cardsum)


a = Player()
b = Dealer() 


print("\n승패 결과는???????")

if a.cardsum == 21 :
    print("완승")

elif a.cardsum > 21:
    print("패")

elif a.cardsum < b.cardsum < 21 :
    print("패")

elif 21 > a.cardsum == b.cardsum :
    print("비김")    

elif 21 > a.cardsum > b.cardsum :
    print("승")    

else : print('GAME RESTART')