  while(self.cardsum < 17):
        
        self.card = Game.game1()

        self.cardlist.append( self.card )
        
        self.num = self.card.lstrip(self.card[0])
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        
        elif  self.num == 'a': pass

        else : self.num = int(self.num)

        self.numberlist.append(self.num)

        print("딜러 while 카드", self.cardlist)

            for x, i in enumerate(self.numberlist):
                
                if x < len(self.numberlist) : continue 
                
                if i == 'a':
                    if (21 - self.cardsum) < 10:
                        i = 11
                    else : 
                        i = 1
                
                self.cardsum += i