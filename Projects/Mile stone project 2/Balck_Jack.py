import random

# Creating deck of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'
         , 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
        'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    # Class for a single card
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank+" of "+self.suit

# Creating a deck of cards

class Deck():
    # Adding cards to deck
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    # Returning individual cards
    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "Deck has: "+ deck_comp
        
    # Shuffling cards
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

test_deck = Deck()
# print(test_deck)

test_deck.shuffle()
print(test_deck)

