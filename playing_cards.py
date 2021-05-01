#python3
#playing-cards

import random

class Playing_Cards:

    def __init__(self):
        pass

    @staticmethod
    def create_deck():
        #tuple
        deck = (
        'AC', '2C', '3C', '4C', '5C', '6C',
        '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
        'AD', '2D', '3D', '4D', '5D', '6D',
        '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
        'AH', '2H', '3H', '4H', '5H', '6H',
        '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
        'AS', '2S', '3S', '4S', '5S', '6S',
        '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS'
        )

        return deck

    @staticmethod
    def shuffle_cards(cards):
        shuffled_cards = list(cards)
        random.shuffle(shuffled_cards)
        return shuffled_cards

    @staticmethod
    def draw_card(cards):
        card_drawn = random.choice(cards)
        cards.remove(card_drawn)
        return card_drawn

    @staticmethod
    def print_deck(cards):
        print(len(cards), cards)




game_deck = Playing_Cards.create_deck()

Playing_Cards.print_deck(game_deck)

shuffled_deck = Playing_Cards.shuffle_cards(game_deck)

Playing_Cards.print_deck(shuffled_deck)

card = Playing_Cards.draw_card(shuffled_deck)

print(card)
Playing_Cards.print_deck(shuffled_deck)
