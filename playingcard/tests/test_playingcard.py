# -*- coding: utf-8 -*-
from playingcard import PlayingCard


class TestPlayingCard():
    """Test the PlayingCard model."""

    def test_create_card_success(self):
        """Verify a card can be created."""
        card = PlayingCard(suit='S', value='A')
        assert card.suit == 'S'
        assert card.value == 'A'

    def test_create_card_suit_fail(self):
        """Verify a card cannot be created with an invalid suit."""
        try:
            card = PlayingCard(suit='A', value='A')
            assert False
        except ValueError as e:
            assert True
            assert "unknown suit" in e.args[0]
        except:
            assert False

    def test_create_card_value_fail(self):
        """Verify a card cannot be created with an invalid value."""
        try:
            card = PlayingCard(suit='C', value='11')
            assert False
        except ValueError as e:
            assert True
            assert "unknown value" in e.args[0]
        except:
            assert False

    def test_card_as_dict_success(self):
        """Verify the as_dict() method."""
        test_suit = 'C'
        test_value = '5'
        card = PlayingCard(suit=test_suit, value=test_value)
        assert card.suit == test_suit
        assert card.value == test_value

        card_dict = card.as_dict()
        assert card_dict['suit'] == test_suit
        assert card_dict['value'] == test_value
        