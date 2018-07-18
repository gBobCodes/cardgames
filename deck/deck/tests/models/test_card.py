from django.test import TestCase

from deck.models import Card


class TestCard(TestCase):
    """Test the Card model."""

    def test_create_card_suit_success(self):
        """Verify a card can be created."""
        card = Card(suit='S', value='A')
        assert card.suit == 'S'
        assert card.value == 'A'

    def test_create_card_suit_fail(self):
        """Verify a card cannot be created with an invalid suit."""
        try:
            card = Card(suit='A', value='A')
            assert False
        except ValueError as e:
            assert True
            assert "unknown suit" in e.args[0]
        except:
            assert False

    def test_create_card_value_fail(self):
        """Verify a card cannot be created with an invalid value."""
        try:
            card = Card(suit='C', value='11')
            assert False
        except ValueError as e:
            assert True
            assert "unknown value" in e.args[0]
        except:
            assert False
