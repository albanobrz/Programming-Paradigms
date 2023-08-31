from card import Card
from deck import Deck
from player import Player

deck = Deck()
playersArray = []

player1 = Player("Bob")
player2 = Player("Alice")
player3 = Player("Fred")

player1.setCards(deck.drawCard(), deck.drawCard())
player2.setCards(deck.drawCard(), deck.drawCard())
player3.setCards(deck.drawCard(), deck.drawCard())

playersArray.append(player1)
playersArray.append(player2)
playersArray.append(player3)

print(player1.name)
player1.getCards()

print(player2.name)
player2.getCards()

print(player3.name)
player3.getCards()

winner = None
highestCard = 2
highestCardSuit = "C"

def compareSuits(suitOfPlayer, suitOfCurrentHighestCard):
    priority_order = ["A", "H", "D", "C"]
    
    return priority_order.index(suitOfPlayer) < priority_order.index(suitOfCurrentHighestCard)

for player in playersArray:
    if player.highestCard > highestCard:
        highestCard = player.highestCard
        highestCardSuit = player.highestCardSuit
        winner = player
    
    if player.highestCard == highestCard:
        if compareSuits(player.highestCardSuit, highestCardSuit):
            highestCardSuit = player.highestCardSuit
            winner = player
        
winner.roundWon()
print(winner.name, highestCard, highestCardSuit, "wins")

print("board:", player1.getRoundsWon(), player2.getRoundsWon(), player3.getRoundsWon())


# write the rules

