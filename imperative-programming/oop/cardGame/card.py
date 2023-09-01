class Card:
    def __init__(self, rank=None, suit=None):
        self.rank = rank
        self.suit = suit
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit

    def cardTranslateRank(self):
        cardsDict = {11: "J", 12: "Q", 13: "K", 14: "A"}
        cardTranslated = self.rank
        if self.rank in cardsDict:
            cardTranslated = cardsDict[self.rank]
        else:
            cardTranslated = str(self.rank)
        
        return cardTranslated
    
    @staticmethod
    def compareSuits(suitOfPlayer, suitOfCurrentHighestCard):
        priority_order = ["S", "H", "D", "C"]
    
        return priority_order.index(suitOfPlayer) < priority_order.index(suitOfCurrentHighestCard)