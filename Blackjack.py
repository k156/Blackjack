class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

    def __str__(s):
        return s

        
from functools import reduce
import random


deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']


class Card:

    def cardprocessor(self):
        random.shuffle(deck)
        self.card = deck.pop()
        print(self.card)

        self.cardlist = []
        self.cardlist = self.cardlist.append(self.card)
        print(self.cardlist)



        self.cardsum = 0
        

        if card[2] == 'j' or 'q' or 'k':
            numberlist.append(10)
        else:
            pass

    def summation(self):
        cardsum = reduce(lambda x, y: x + y, numberlist)


class Player(Card):
    a_value = ''
    def game(self):
        self.card = Card.card()
        if card[2] == 'a':
            while (a_value ==''):
                a_value = input("A값을 1과 11중에 선택하세요.")
                if a_value == 1:
                    numberlist.append(1)
                elif a_value == 11:
                    numberlist.append(11)
                else:
                    continue
        Card.summation(numberlist)

    game()
    if cardsum == 21:
        print("승")
    elif cardsum > 21:
        print("패")
    else:
        while (cardsum <21):
            hit = input("카드를 더 받으려면 'hit', 그만 받으려면 'stand'를 입력하세요.")
            if hitorstand == 2:
                break
                if Dealer.cardsum == Player.cardsum:
                    print("비겼습니다.")
                elif Dealer.cardsum > Player.cardsum:
                    print("패")
                else:
                    game()
                
                                        

class Dealer(Game):
    Card.card()
    def reveal(self):
        print(cardlist[0])
    

# ===================main flow========================
gamestart = ''

while (gamestart == ''):
    gamestart = input("게임을 시작하려면 엔터를 누르세요.")
    player = Player()
    dealer = Dealer()
