import random
from functools import reduce
import os



class Game:
  
    def __init__(self):

        self.cardlist = []          
        self.numberlist = [] 
    
    @staticmethod
    def game1():
        deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']
        random.shuffle(deck)
        card = deck.pop()
        return card

    def game2(self):        
      
        self.card = Game.game1()

        self.cardlist.append( self.card )
        
        self.num = self.card.lstrip(self.card[0])
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        
        elif  self.num == 'a': pass

        else : self.num = int(self.num)

        self.numberlist.append(self.num)

        # print(self.cardlist)
        # print(self.numberlist)
    

    # def cardsummation(self):

    #     self.cardsum = reduce(lambda x, y: x + y, self.numberlist)       
           
      

class Player(Game):
    def __init__(self):
        super().__init__()
        self.cardsum = 0
        self.game2()
        for i in self.numberlist:
            if i == 'a':
                input_a = input ("a의 값 결정 (1 = 1 입력, 11 = 11 입력) >> ")
                if input_a == '1':
                    i = 1
                elif input_a == '11':
                    i = 11
                    # break
            
            self.cardsum += i
        
        
        print("플레이어 초기 넘버리스트", self.numberlist)

        while( self.cardsum < 21): 
            self.game2()

            for x, i in enumerate(self.numberlist):
                if x < len(self.numberlist) : continue 
                
                if i == 'a':
                    input_a = input ("a의 값 결정 (1 = 1 입력, 11 = 11 입력) >> ")
                    if input_a == '1':
                        i = 1
                    elif input_a == '11':       
                        i = 11
                        # break
                
                self.cardsum += i

            print("플레이어의 카드>>>", self.cardlist) 
            
            if self.cardsum == 21: 
                # os.system('CLS')
                print("플레이어의 카드>>>", self.cardlist) 
                print("플레이어의 카드 총 합>>>", self.cardsum)
                
            elif self.cardsum > 21:
                # os.system('CLS')
                print("플레이어의 카드>>>", self.cardlist) 
                print("플레이어의 카드 총 합>>>", self.cardsum) 
                

            elif self.cardsum < 21: 
                hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.") 


                if hitorstand == '1': 
                    continue 


                elif hitorstand == '2':  
                    # os.system('CLS')
                    print("플레이어의 카드>>>", self.cardlist) 
                    print("플레이어의 카드 총 합>>>", self.cardsum) 
                    break 
     
        
       
         
class Dealer(Game):
    def __init__(self):
        
        super().__init__()
        self.game2()
        self.cardsum = 0
        for i in self.numberlist:
            if i == 'a':
                if (21 - self.cardsum) < 10:
                    i = 11
                else : 
                    i = 1
            
            self.cardsum += i
        
        print("딜러 초기 카드", self.cardlist)

        while(self.cardsum < 17):
            self.game2()
            
            print("딜러 while 카드", self.cardlist)

            for x, i in enumerate(self.numberlist):
                
                if x < len(self.numberlist) : continue 
                
                if i == 'a':
                    if (21 - self.cardsum) < 10:
                        i = 11
                    else : 
                        i = 1
                
                self.cardsum += i
        
        print("딜러의 카드리스트>>>",self.cardlist)
        print("딜러의 카드 총 합>>>",self.cardsum)

# a.cardlist()
a = Player()
b = Dealer() 


print("\n승패 결과는???????")  
 
if a.cardsum == 21 : 
     print("완승") 
  
 
elif a.cardsum > 21: 
      print("패") 
  
elif a.cardsum < 21 and b.cardsum > 21:  
      print("승") 

elif a.cardsum < b.cardsum < 21 : 
      print("패") 
  
 
elif 21 > a.cardsum == b.cardsum : 
      print("비김")     
  
 
elif 21 > a.cardsum > b.cardsum : 
      print("승")     
 

