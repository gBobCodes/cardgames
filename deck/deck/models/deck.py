import json, random
from playingcard import PlayingCard


class Deck():
    """A list of 52 playing cards, 54 if jokers are included."""

    def __init__(self, jokers=False):
        """Initialize an ordered list of 52 playing cards, 54 if jokers."""
        self.cards = []
        for suit in PlayingCard.valid_suits:
            for value in PlayingCard.valid_values:
                self.cards.append(PlayingCard(suit=suit, value=value))

        if jokers:
            for suit in PlayingCard.valid_joker_suits:
                for value in PlayingCard.valid_joker_values:
                    self.cards.append(PlayingCard(suit=suit, value=value))

    def show_cards(self):
        """Print out a nice display of the cards in the deck."""
        for card in self.cards:
            print(card)
        
    def shuffle(self):
        """Randomly order the list of cards."""
        random.shuffle(self.cards)

    def json_cards(self):
        """Return a list of the cards as dictionaries."""
        card_list = []
        for card in self.cards:
            card_list.append(card.as_dict())
        return card_list