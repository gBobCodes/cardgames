import copy
from django.test import TestCase

from deck.models import Deck


class TestDeck(TestCase):
    """Test the Deck model."""

    def test_create_deck_no_jokers_success(self):
        """Verify a deck can be created without jokers."""
        deck = Deck()
        assert len(deck.cards) == 52

    def test_create_deck_with_jokers_success(self):
        """Verify a deck can be created with jokers."""
        deck = Deck(jokers=True)
        assert len(deck.cards) == 54

    def test_shuffle_success(self):
        """Verify the shuffle method does change the order of the cards."""
        deck = Deck()
        not_shuffled_cards = copy.deepcopy(deck.cards)
        shuffled_cards = deck.cards
        assert not_shuffled_cards[0].suit == shuffled_cards[0].suit
        assert not_shuffled_cards[0].value == shuffled_cards[0].value

        deck.shuffle()

        shuffled = False
        for i in range(len(not_shuffled_cards)):
            if all([
                not_shuffled_cards[i].suit != shuffled_cards[i].suit,
                not_shuffled_cards[i].value != shuffled_cards[i].value
            ]):
                shuffled = True
        assert shuffled

    def test_json_cards_success(self):
        """Verify the json_cards() method returns a list of dictionaries."""
        deck = Deck()
        deck.shuffle()
        json_cards = deck.json_cards()
        for i in range(len(json_cards)):
            assert json_cards[i]['suit'] == deck.cards[i].suit
            assert json_cards[i]['value'] == deck.cards[i].value
