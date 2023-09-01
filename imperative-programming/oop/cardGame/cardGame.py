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
            if Card.compareSuits(player.highestCardSuit, highestCardSuit):
                highestCardSuit = player.highestCardSuit
                winner = player
            
    winner.roundWon()
    
    print(winner.name, "wins with", Card(highestRank, None).cardTranslateRank(), highestCardSuit)

    print("\nboard:") 
    for player in playersArray:
        player.getNameAndRoundsWon()
    
print("GG")