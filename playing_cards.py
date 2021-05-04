#python3
#playing-cards

class Playing_Cards:

    def __init__(self, deck_name):
        self.deck_name = deck_name

    def create_deck():
        #tuple
        deck_name = (
        'AC', '2C', '3C', '4C', '5C', '6C',
        '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
        'AD', '2D', '3D', '4D', '5D', '6D',
        '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
        'AH', '2H', '3H', '4H', '5H', '6H',
        '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
        'AS', '2S', '3S', '4S', '5S', '6S',
        '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS'
        )

        return deck_name

    @staticmethod
    def shuffle_cards(cards):
        import random
        shuffled_cards = list(cards)
        random.shuffle(shuffled_cards)
        return shuffled_cards

    @staticmethod
    def draw_card(cards):
        import random
        card_drawn = random.choice(cards)
        cards.remove(card_drawn)
        return card_drawn

    @staticmethod
    def draw_cards(cards, qty):
        import random
        if qty < len(cards):
            cards_drawn = []
            for card in range(qty):
                cards_drawn.append(random.choice(cards))
                cards.remove(cards_drawn[card])
            return cards_drawn
        else:
            print('Draw Card Error. Not enough cards to draw.')


    @staticmethod
    def print_cards(cards):
        print(len(cards), sorted(cards))

    @staticmethod
    def discard(cards):
        #discards random card from the deck - user is unaware of discarded card
        cards.remove(random.choice(cards))



#
# game_deck_1 = Playing_Cards.create_deck()
#
# Playing_Cards.print_cards(game_deck_1)
#
# shuffled_deck_1 = Playing_Cards.shuffle_cards(game_deck_1)
#
# Playing_Cards.print_cards(shuffled_deck_1)
#
#
#
# game_deck_2 = Playing_Cards.create_deck()
#
# Playing_Cards.print_cards(game_deck_2)
#
# shuffled_deck_2 = Playing_Cards.shuffle_cards(game_deck_2)
#
# Playing_Cards.print_cards(shuffled_deck_2)




#
# card = Playing_Cards.draw_card(shuffled_deck_1)
# #
# print(card)
# card = Playing_Cards.draw_card(shuffled_deck_1)
# #
# print(card)
# card = Playing_Cards.draw_card(shuffled_deck_1)
# #
# print(card)
# card = Playing_Cards.draw_card(shuffled_deck_1)
# #
# print(card)
# Playing_Cards.print_cards(shuffled_deck_1)


# Playing_Cards.print_deck(shuffled_deck)
#
# Playing_Cards.discard(shuffled_deck)
#
# Playing_Cards.print_deck(shuffled_deck)

# my_hand = Playing_Cards.draw_cards(shuffled_deck, 55)
#
# Playing_Cards.print_deck(shuffled_deck)
#
# print(my_hand)
