from card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.roundWins = 0
        self.card1 = None
        self.card2 = None
        self.highestCard = 2
        self.highestCardSuit = "C"
        
    def roundWon(self):
        self.roundWins += 1
    
    def getRoundsWon(self):
        return self.roundWins
    
    def setCards(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
    
    def getCards(self):
        if self.card1 != None and self.card2 != None:
            print(self.card1.rank, self.card1.suit, "/", self.card2.rank, self.card2.suit)
            self.setHighestCard()
    
    def setHighestCard(self):
        if self.card1.rank >= self.card2.rank:
            self.highestCard = self.card1.rank
            self.highestCardSuit = self.card1.suit
        else:
            self.highestCard = self.card2.rank
            self.highestCardSuit = self.card2.suit
            