from card import Card
from deck import Deck
from player import Player

deck = Deck()
playersArray = []

player1 = Player("Bob")
player2 = Player("Alice")
player3 = Player("Fred")

playersArray.append(player1)
playersArray.append(player2)
playersArray.append(player3)

deck.getTotalCards()

print("the game will begin...")

def compareSuits(suitOfPlayer, suitOfCurrentHighestCard):
    priority_order = ["A", "H", "D", "C"]
    
    return priority_order.index(suitOfPlayer) < priority_order.index(suitOfCurrentHighestCard)

while deck.totalCards >= (len(playersArray)*2):
    input("Press Enter to continue or ctrl+c to exit\n")
    
    for player in playersArray:
        player.setCards(deck)
        player.getPlayerName()
        player.getCards()

    deck.getTotalCards()

    # reset rank
    winner = None
    highestRank = 2
    highestCardSuit = "C"

    for player in playersArray:
        if player.highestCard > highestRank:
            highestRank = player.highestCard
            highestCardSuit = player.highestCardSuit
            winner = player
        
        if player.highestCard == highestRank:
            if compareSuits(player.highestCardSuit, highestCardSuit):
                highestCardSuit = player.highestCardSuit
                winner = player
            
    winner.roundWon()
    
    print(winner.name, "wins with", Card(highestRank, None).cardTranslateRank(), highestCardSuit)

    print("board:\n", 
        player1.name, ":", player1.getRoundsWon(), 
        player2.name, ":",player2.getRoundsWon(), 
        player3.name, ":",player3.getRoundsWon())
    
print("GG")