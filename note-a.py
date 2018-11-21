 self.cardsum = reduce(lambda x, y: x + y, self.numberlist)      
    if x == 'a' or y == 'a':    
        if (21 - self.cardsum) <= 10:
            return 11
        else :
            return 1


