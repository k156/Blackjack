import random

class Deck:

    def card():
        deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']
        
        card = random.pop(deck)
        
        return card
        

class Card:

    def start_cardlist(self):
        while(len(cardlist) < 2):
        
        self.card = Deck.card()
        
        cardlist = []
        self.cardlist = cardlist.append( self.card )

        print(self.cardlist)

        

    def cardsum(self):
            
            cardsum = 0

            for i in self.cardlist:

                if (i[1]) == 'a':
                    input_a = input("a를 1로 하겠습니까? -> 1입력 아니면 11로 하겠습니까? -> 11입력")
                    if input_a == '11' or input_a == '1':
                        i[1] = int(input_a)
                    else :
                        print("다시입력하세요")

                elif (i[1]) == "q" or (i[1]) == "k" or (i[1]) == "j":
                    i[1] = 10

                self.cardsum = self.cardsum + i[1]          

class Player:

input_msg = input ("hit or stand (hit : 1, stand : 2 -->")

class Dealer:


