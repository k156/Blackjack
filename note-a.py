# import random

# class Deck:

#     def card():
#         deck_m = ['heart', 'spade', 'diamond', 'clover']
#         deck_s = ['a',2,3,4,5,6,7,8,9,10,'q','k','j']
        
#         print([random.choice(deck_m), random.choice(deck_s)])
        
     
# Deck.card()


card = ['q1','q2','s11','d1']
num = []

for i in card:
    
   num.append(i.lstirp(i[0]))

print(num)



# 정민님 card class

# class Card:

#    def __init__(self):
#        random.shuffle(deck)
#        self.card = deck.pop()

#        self.cardlist = []
#        self.cardlist.append(self.card)
#        print(self.cardlist)

#        self.numberlist = []
#        self.numberlist.append(Casting.to_int(self.card.lstrip(self.card[0])))

#        print(self.numberlist)