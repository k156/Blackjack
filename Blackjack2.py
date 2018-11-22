import random
from functools import reduce
class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

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
        self.cardlist.append(self.card)
        
        print("card>>>", self.card)
        print("cardlist>>>", self.cardlist)
    
        self.num = self.card.lstrip(self.card[0])
        print("num>>>", self.num)
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        elif self.num == 'a':
            pass
        else:
            self.num = Casting.to_int(self.num)

        print("intnum>>>", self.num)
    
    
    def has_a(self):
        a_value = 0
        if self.num == 'a':
            while (a_value == False):
                a_value = input("A값을 1과 11중에 선택하세요.")
                if a_value == 1:
                    self.num = 1
                    print("a_value>>>",self.num)
                    break

                elif a_value == 11:
                    self.num = 1
                    break

                else:
                    continue


    def append_to_numberlist(self):
            self.numberlist.append(self.num)
            print("numberlist>>>", self.numberlist)

    def summation(self):
        self.cardsum = reduce(lambda x, y: x + y, self.numberlist)  
        print("cardsum>>>", self.cardsum)


# g = Game()
# g.game2()
# g.game2()
# g.summation()


class Player(Game):
    def play_game(self):
        self.game2()
        self.has_a()
        self.append_to_numberlist()
        self.game2()
        self.has_a()
        self.append_to_numberlist()
        self.summation()
       

p = Player()
p.play_game()
        
        
         
# class Dealer(Game):
#     def __init__(self):
#         self.game1()
#         self.cardsummation()
#         while(self.cardsum < 21):
#             self.game1()
#             self.cardsummation()

        
        
#         print(self.cardlist)
#         print("딜러의 카드 총 합>>>",self.cardsum)

# # a.cardlist()
# a = Player()
# b = Dealer() 

# # while(a.cardsum < 21):
    
# #     if a.cardsum == 21:   print("승")

# #     elif a.cardsum > 21:   print("패")

# #     elif a.cardsum < 21:
# #         hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.")
        
# #         if hitorstand == '1':   
# #             continue

# #         if hitorstand == '2': 
# #             print(a.cardsum)
# #             break



# # while(b.cardsum < 17)

# #     if b.cardsum == 21:   
# #         print(b.cardsum)
# #         break

# #     elif b.cardsum > 21:   
# #         print("player 승")



# print("승패 결과는???????")
# if a.cardsum < b.cardsum :
#     print("승")

# elif a.cardsum == b.cardsum :
#     print("비김")    

# elif a.cardsum > b.cardsum :
#     print("패")  