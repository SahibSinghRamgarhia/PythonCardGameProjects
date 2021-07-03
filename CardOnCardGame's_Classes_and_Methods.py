import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# 1st Class :- Card! It consists a method which creates a card with its 'suit', 'rank' & 'value'.
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# 2nd Class :- Deck! It consists methods which create my_deck of 52 cards, shuffle it & deal with one card at a time.
class Deck:

    def __init__(self):
        self.all_cards = []
        for each_suit in suits:
            for each_rank in ranks:
                created_card = Card(each_suit, each_rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# 3rd Class :- Player! It consists methods which can remove & add a card from/in player's hand( a list of cards ).
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            # type(new_cards) == type([]) is similar to isinstance(new_cards, list)
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# Now it's time to write some logic :-
player_one = Player('ONE')
player_two = Player('TWO')

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player ONE is out of cards :(  Player TWO wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two is out of cards :(  Player ONE wins!')
        game_on = False
        break

    # Start a new round
    # player_one_cards = []
    # player_one_cards.append(player_one.remove_one_card())
    player_one_cards = [player_one.remove_one_card()]

    player_two_cards = []
    player_two_cards.append(player_two.remove_one_card())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!!!')

            if len(player_one.all_cards) < 5:
                print('Player ONE unable to declare War :(')
                print('Player TWO Wins!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player TWO unable to declare War :(')
                print('Player ONE Wins!')
                game_on = False
                break

            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove_one_card())
                    player_two_cards.append(player_two.remove_one_card())