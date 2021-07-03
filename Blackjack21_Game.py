import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


# Step 1 :- (Class : Card!) It is used to create cards with their respective suits and ranks.
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# Step 2 :- (Class : Deck!) It is used to create a deck of 52 cards, shuffle it & take one card at a time from the deck.
class Deck:

    def __init__(self):
        self.deck = []
        for each_suit in suits:
            for each_rank in ranks:
                created_card = Card(each_suit, each_rank)
                self.deck.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()

    def __str__(self):
        deck_comp = ''
        for each_card in self.deck:
            deck_comp += '\n' + each_card.__str__()
        return "The my_deck has : " + deck_comp


# Step 3 :- (Class : Hand!) It is used to hold player's cards and check the total values of the cards A/W/A check aces.
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        # tracking aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If self.value is greater than 21 and i still have an aces, then change my ace value to 1 instead of an 11.
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


# Step 4 :- (Class : Chips!) It is used to raise bets and check the results of the bets raised by the players.
class Chips:

    def __init__(self, total):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Step 5 :- Function for taking bets from the user :-
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips you want to bet? '))
        except:
            print('Please provide an integer value!')
        else:
            if chips.bet > chips.total:
                print("Sorry! You don't have enough chips. You have : {} chips.".format(chips.total))
            else:
                break


# Step 6 :- Function for taking hits :-
def hit(deck, hand):
    single_card = deck.deal_one()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# Step 7 :- Function prompting the player to Hit or Stand :-
def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand ? Enter h or s :- ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands, Dealer's turn")
            playing = False

        else:
            print("I didn't understand that, please enter h and s only!")
            continue
        break


# Step 8 :- Functions to display cards.
def show_some(player, dealer):
    # show only one of the dealer's card
    print("\n Dealer's hand : ")
    print("First card hidden")
    print(dealer.cards[1])

    # show all ( 2 cards ) of the player's hand/cards
    print("\n Player's hand : ")
    for each_card in player.cards:
        print(each_card)


def show_all(player, dealer):
    # show all the dealer's cards
    print("\n Dealer's hand : ")
    for each_card in dealer.cards:
        print(each_card)

    # Calculate and display Dealer's hand value
    print(f"Value of Dealer's hand is : {dealer.value}")

    # show all the player's cards
    print("\n Player's hand : ")
    for each_card in player.cards:
        print(each_card)

    # Calculate and display Player's hand value
    print(f"Value of Player's hand is : {player.value}")


# Step 9 :- Functions to handle end of game scenario
def player_busts(chips):
    print("Player Busted! Dealer Wins!")
    chips.lose_bet()


def player_wins(chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer Busted! Player Wins!")
    chips.win_bet()


def dealer_wins(chips):
    print("Dealer Wins!")
    chips.lose_bet()


def push():
    print("Dealer and Player Tie! PUSH")


# NOW IT'S TIME TO WRITE CODE BY USING ALL THE CLASSES, METHODS & LOGIC WE HAD MADE TO RUN THE GAME :-

# Set up the player chips
player_chips = Chips(100)

while True:
    # An opening statement For the game
    print('Welcome to BLACKJACK_21')

    # Create & Shuffle the my_deck, deal two cards for each player
    my_deck = Deck()
    my_deck.shuffle_deck()

    player_hand = Hand()
    player_hand.add_card(my_deck.deal_one())
    player_hand.add_card(my_deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(my_deck.deal_one())
    dealer_hand.add_card(my_deck.deal_one())

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:

        # Prompt for player to hit or stand
        hit_or_stand(my_deck, player_hand)

        # Show some cards
        show_some(player_hand, dealer_hand)

        # if player_hand exceeds 21, run player_bust() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # if player hasn't busted play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(my_deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenario
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    # Inform player of their chips total
    print("\nPlayer's total chips are at {}".format(player_chips.total))

    # Ask to play again
    another_round = input("Would you like to play another round? yes or no :- ")
    if another_round[0].lower() == 'y':
        playing = True
        continue
    else:
        print("ThankYou for playing!")
        break