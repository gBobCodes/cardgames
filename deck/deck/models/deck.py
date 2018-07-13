import random

from .card import Card


class Deck():
    """A list of 52 playing cards, 54 if jokers are included."""

    def __init__(self, jokers=False):
        """Initialize an ordered list of 52 playing cards, 54 if jokers."""
        self.cards = []
        for suit in Card.valid_suits:
            for value in Card.valid_values:
                self.cards.append(Card(suit=suit, value=value))

        if jokers:
            for suit in Card.valid_joker_suits:
                for value in Card.valid_joker_values:
                    self.cards.append(Card(suit=suit, value=value))

    def show_cards(self):
        """Print out a nice display of the cards in the deck."""
        for card in self.cards:
            print(card)
        
    def shuffle(self):
        """Randomly order the list of cards."""
        print("shuffling . . .")
        random.shuffle(self.cards)
        print("done")

