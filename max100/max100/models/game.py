import random, requests

from max100.models import PlayableCard

class Game():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.discard_pile = []
        self.draw_pile = []
        self.players = []

    def assign_points(self):
        """Assign points to each card based on it's value."""
        for card in self.draw_pile:
            if card.value == 'A':
                card.points = 1
            elif card.value in ['K', 'Q', 'J', '10']:
                card.points = 10
            elif card.value == '9':
                card.points = 0
            elif card.value == '5':
                card.points = [-5, 5]
            else:
                card.points = int(card.value)

    def convert_discard_to_draw_pile(self):
        """The draw pile is empty, shuffle discard, make them the draw pile."""
        if self.discard_pile and not self.draw_pile:
            self.draw_pile = self.discard_pile
            self.discard_pile = []
            random.shuffle(self.draw_pile)

    def new_deck(self):
        """Start a new game by getting a new deck of cards."""
        r = requests.get("http://localhost:8000/deck")
        self.draw_pile = []
        self.discard_pile = []
        for item in r.json():
            card = PlayableCard(
                suit=item['suit'],
                value=item['value'],
                points=None
            )
            self.draw_pile.append(card)
        self.assign_points()


