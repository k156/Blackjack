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
        
        self.cardlist = []        
        self.numberlist = [] 
        

    def mk_cardlist(self):
        global g_deck
        self.card = g_deck.pop(0)
        self.cardlist.append( self.card )
        
    
    def mk_numberlist(self):    
        
        self.num = self.card.lstrip(self.card[0])
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        
        elif  self.num == 'a': pass

        else : self.num = Casting.to_int(self.num)

        self.numberlist.append(self.num)

    def cardsummation(self):
        ret = 0
        for i in self.numberlist:
            if i == 'a':
                if (21 - self.cardsum) <= 10:
                    i = 11
                else:
                    i = 1

            ret += i

        self.cardsum = ret

        return ret

        # self.cardsum = reduce(self.xxxx, self.numberlist) 


class Player(Card):
    def __init__(self):
        super().__init__()
        super().mk_cardlist()
        super().mk_numberlist()

        while(Player.cardsummation() < 21):
            super().mk_cardlist()
            super().mk_numberlist()
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

    @staticmethod
    def cardsummation(self):
            ret = 0
            for i in self.numberlist:
                if i == 'a':
                    input_a = input("a를 1로 하겠습니까? -> 1입력 아니면 11로 하겠습니까? -> 11입력")
                    if input_a == '11' or input_a == '1':
                        i = int(input_a)
                    else :
                        print("다시입력하세요")
                            
                ret += i

            self.cardsum = ret

            return ret       


         
class Dealer(Card):
    def __init__(self):
        
        super().__init__()
        super().mk_cardlist()
        super().mk_numberlist()
     
        while(self.cardsummation() < 17):
            super().mk_cardlist()
            super().mk_numberlist()
            
        print("딜러의 카드>>", self.cardlist)
        print("딜러의 카드 합>>>", self.cardsum)
            

a = Player()
b = Dealer() 


print("승패 결과는???????")
if a.cardsum < b.cardsum < 21 :
    print("승")

elif 21 > a.cardsum == b.cardsum :
    print("비김")    

elif 21 > a.cardsum > b.cardsum :
    print("패")    
