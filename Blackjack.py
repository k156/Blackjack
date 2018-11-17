class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

    def __str__(s):
        return s

class Deck:
    deck_m = ['heart', 'spade', 'diamond', 'clover']
    deck_s = ['a',2,3,4,5,6,7,8,9,10,'q','k','j']
    shape, number = '',''
    
    def randomcard():
        import random
        shape = random.choice(deck_m)
        number = random.choice(Casting.to_int(deck_s))
        

class Card:
    from functools import reduce
    
    cardlist = []
    numberlist = []
    cardsum = 0

    def cardprocess(self):
        card = [Deck.randomcard(shape), Deck.randomcard(number)]
        cardlist.append(card) 
        print(cardlist)

        if card[2] == 'j' or 'q' or 'k':
            numberlist.append(10)
        else:
            pass

    def summation(self):
        cardsum = reduce(lambda x, y: x + y, numberlist)


class Player(Card):
    a_value = ''
    def game(self,numberlist):
        Card.cardprocess()
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
    Card.cardprocess()
    def reveal(self):
        print(cardlist[0])
    

# ===================main flow========================
gamestart = ''

while (gamestart == ''):
    gamestart = input("게임을 시작하려면 엔터를 누르세요.")
    player = Player()
    dealer = Dealer()
