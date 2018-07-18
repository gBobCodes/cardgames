# from django.db import models


# class Card(models.Model):
class Card():
    """A playing card with a suit and a value."""

    valid_suits = ['S', 'H', 'C', 'D']  # Spade, Heart, Club, Diamond
    valid_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    valid_joker_suits = ['B', 'R']      # Black, Red
    valid_joker_values = ['JOKER']

    def __init__(self, suit, value):
        """Initialize a card with the given parameters."""
        suit = suit.upper()
        value = value.upper()
        if suit not in self.valid_suits + self.valid_joker_suits:
            raise ValueError(
                'You gave me an unknown suit: {}. Try one of these {}'.format(
                    suit,
                    self.valid_suits
                )
            )
        if value not in self.valid_values + self.valid_joker_values:
            raise ValueError(
                'You gave me an unknown value: {}. Try one of these {}'.format(
                    value,
                    self.valid_values
                )
            )

        self.suit = suit
        self.value = value

    def __str__(self):
        """Return a string for the print() command."""
        return "{} {}".format(self.value, self.suit)

    def as_dict(self):
        """Return a dictionary of this card's values."""
        return {
            "suit": self.suit,
            "value": self.value,
        }


class PlayableCard(Card):
    
    def __init__(self, suit, value, points=0):
        """Initialize a card with the given parameters."""
        super().__init__(suit, value)
        self.points = points

    def __str__(self):
        """Return a string for the print() command."""
        return "{} {}".format(super().__str__(), self.points)

    def as_dict(self):
        """Return a dictionary of this card's values."""
        a_dict = super().as_dict()
        a_dict['points'] = self.points
        return a_dict
