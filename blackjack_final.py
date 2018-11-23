import random
from functools import reduce
import os
  
class Game:
  
    def __init__(self):

        self.cardlist = []          
        self.numberlist = [] 
        self.cardsum = 0
        global g_deck
        

    def game2(self):

        self.card = g_deck.pop()
        self.cardlist.append(self.card)

        self.num = self.card.lstrip(self.card[0])
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10

        elif self.num == 'a':
            pass

        else:
            self.num = int(self.num)

        self.numberlist.append(self.num)
      



class Player(Game):
    def __init__(self):
        
        super().__init__()
        self.game2()
        
        for i in self.numberlist:
                
            if i == 'a':
                print("플레이어의 카드>>>", self.cardlist) 
                input_a = input ("a의 값 결정 (1 = 1 입력, 11 = 11 입력) >> ")
                if input_a == '1':
                    i = 1
                elif input_a == '11':       
                    i = 11
            
            self.cardsum += i
   
        
    def player_play(self):

        while( self.cardsum < 21): 
           
            self.game2()

            for x, i in enumerate(self.numberlist):
                
                if len(self.numberlist) >= 2 and x < ( len(self.numberlist) - 1 ): continue 

                if i == 'a':
                    print("플레이어의 카드>>>", self.cardlist) 
                    input_a = input ("a의 값 결정 (1 = 1 입력, 11 = 11 입력) >> ")
                    if input_a == '1':
                        i = 1
                    elif input_a == '11':       
                        i = 11
                
                self.cardsum += i
            
            print("플레이어의 카드>>>", self.cardlist) 

            if self.cardsum == 21: 
                self.player_print()
                
            elif self.cardsum > 21:
                self.player_print()

            elif self.cardsum < 21: 

                hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.")

                if hitorstand == '1': 
                    continue 

                elif hitorstand == '2':  
                    self.player_print()
                    break 


    def player_print(self):
        os.system('CLS')
        print("플레이어의 카드>>>", self.cardlist) 
        print("플레이어의 카드 총 합>>>", self.cardsum) 


class Dealer(Game):
    def __init__(self):
        
        super().__init__()
        self.game2()

        for i in self.numberlist:
            if i == 'a':
                    if self.cardsum <= 10:
                        i = 11
                    else : 
                        i = 1
            self.cardsum += i
        
        print("딜러의 카드리스트>>>",self.cardlist)

    def dealer_play(self):
        while( self.cardsum < 17 ):
        
            self.game2()
            
            for x, i in enumerate(self.numberlist):
                
                if len(self.cardlist) >= 2 and x < ( len(self.cardlist)- 1 ): continue 
                
                if i == 'a':
                    if self.cardsum <= 10:
                        i = 11
                    else : 
                        i = 1
            
                self.cardsum += i
        
        print("\n")
        print("딜러의 카드리스트>>>",self.cardlist)
        print("딜러의 카드 총 합>>>",self.cardsum)



#================= MAIN =====================


def over_21(a,b):

    if a < 21 and b < 21:
        if a > b : print("승") 
        elif a == b : print("비김")
        elif a < b : print("패")
    
    elif a < 21 and b > 21:  print("승")       
    elif a > 21 : print("패")
    elif a == 21 : print("승")
    elif a != 21 and b == 21: print("패")   


while(True):
    print("\n")
    start_game = input("게임을 시작하려면 엔터를 누르세요")
    os.system('CLS')

    if start_game == '':
        
        g_deck = ['♠a','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠j','♠q','♠k',
                '♣a','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣j','♣q','♣k',
                '♥a','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥j','♥q','♥k',
                '◆a','◆2','◆3','◆4','◆5','◆6','◆7','◆8','◆9','◆10','◆j','◆q','◆k']

        random.shuffle(g_deck) 

        a = Player()
        b = Dealer()
        
        a.player_play()
        b.dealer_play()
       
        print("\n승패 결과는???????") 
        over_21(a.cardsum, b.cardsum)
        
    else : break    
          

#================ FLOW =======================