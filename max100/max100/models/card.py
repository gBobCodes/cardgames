from playingcard import PlayingCard

class PlayableCard(PlayingCard):
    
    def __init__(self, suit, value, points=None):
        """Initialize a card with the given parameters."""
        super().__init__(suit, value)
        self.points = points

    def __str__(self):
        """Return a string for the print() command."""
        return "{} {}".format(super().__str__(), self.points)

    def as_dict(self):
        """Return a dictionary of this card's values."""
        return vars(self)

