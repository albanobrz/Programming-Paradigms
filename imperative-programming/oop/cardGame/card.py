class Card:
    def __init__(self, rank=None, suit=None):
        self.rank = rank
        self.suit = suit
    
    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
