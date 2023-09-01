from card import Card
from deck import Deck

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
    
    def setCards(self, deck):
        self.card1 = deck.drawCard()
        self.card2 = deck.drawCard()
    
    def getCards(self):   
        if self.card1 != None and self.card2 != None:
            print(self.card1.cardTranslateRank(), self.card1.suit, "/", self.card2.cardTranslateRank(), self.card2.suit)
            self.setHighestCard()
    
    def setHighestCard(self):
        if self.card1.rank >= self.card2.rank:
            self.highestCard = self.card1.rank
            self.highestCardSuit = self.card1.suit
        else:
            self.highestCard = self.card2.rank
            self.highestCardSuit = self.card2.suit
        
    def getPlayerName(self):
        print(self.name)