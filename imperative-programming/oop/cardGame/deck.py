from card import Card
import random

class Deck:
    def __init__(self):
        self.totalCards = 52
        self.cardsDump = 0
        self.drawnCards = []
    
    def drawCard(self):
        card = Card(random.randint(2, 14), self.getRandomSuit())
        for c in self.drawnCards:
            if card.rank == c.rank and card.suit == c.suit:
                return self.drawCard()
        self.totalCards -= 1
        self.cardsDump += 1
        self.deactivateCard(card)
        return card
    
    def getRandomSuit(self):
        suitRandomNumber = random.randint(1, 4)
        match suitRandomNumber:
            case 1:
                return "H"
            case 2:
                return "C"
            case 3:
                return "D"
            case 4: 
                return "A"
    
    def deactivateCard(self, card):
        self.drawnCards.append(card)
            
    def getTotalCards(self):
        return print(f"there is {self.totalCards} cards in the deck")