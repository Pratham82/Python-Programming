import random

# Creating deck of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'
         , 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
        'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    # Class for a single card
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank+" of "+self.suit

# Creating a deck of cards

class Deck:
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

class Hand():
    def __init__(self):
        self.cards = [] # similar to deck we  start of with an empty list
        self.value = 0  # Total value of the player's cards
        self.aces = 0   # Aces have value of either 1 or 11

    def add_card(self,card):
        self.cards.append(card) # We are grabbing the card from deal method inside deck class  
        self.value += values[card.rank] # passing rank into values dictionary

        # Tracking ace values
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        # If total value is greater than 21 and we have an ace which has value 11
        # Then change the ace's value to 1 to get our total below 21
        # Here self.aces has value of 0 (which will be treated as false), other number will be true
        # so the condition becomes true, only if the value of self.aces > 0
        while self.value > 21 and self.aces :
            self.value -= 10 
            self.aces -= 1

# Creating chips 
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.bet += self.bet
        
    def lose_bet(self):
        self.bet -= self.bet 

# Functions for playing games
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter how many chips you want to bet: "))
        except:
            print("Please add an interger value")
        else:
            if chips.bet > chips.total:
                print(f"Sorry you don't have enough chips, you have {chips.total} chips")
            else:
                break

# Function for taking hits
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # for using while loop
    
    while True:
        x = input("Hit or stand?, enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player stands dealer's turn")
            playing = False

        else:
            print("Sorry wrong input, Please enter 'h'  or 's' ")
            continue
        break

# Show cards method
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

# End of the game scenarios
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and player tied, push")

# Actual game board stars here
while True:
    print("Welcome to blackjack")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    # Creating player's cards 
    player_hand = Hand()
    player_hand.add_card(deck.deal())  # Card 1
    player_hand.add_card(deck.deal())  # Card 2

    # Creating dealers's cards 
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())  # Card 1
    dealer_hand.add_card(deck.deal())  # Card 2

    # Set up the Player's chips
    player_chips = Chips() # with 100 default value 

    # Prompt the Player for their bet:
    take_bet(player_chips)

    # Show the cards:
    show_some(player_hand,dealer_hand)

    while playing:
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)

        # Show card but keep dealer's cards hidden
        show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21 run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until it reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

            # show all cards
        show_all(player_hand,dealer_hand)

            # Run different winning scenario
        if dealer_hand.value >21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand,player_chips)

    # Inform Player of their chips total 
    print(f"\n Player total chips are at {player_chips.total}")   
    
    # Ask the player to play agin
    new_game = input("Do you want to player another hand?  enter 'y' or 'n':  ")
    if new_game[0].lower() == 'y':
        playing =True
        continue
    else:
        print("Thanks for playing!!")
        break
