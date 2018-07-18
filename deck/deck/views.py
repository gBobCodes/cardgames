from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from deck.models import Deck

class DeckView(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """Return a shuffled deck of cards in json format."""
        deck = Deck()
        deck.shuffle()
        return Response(deck.json_cards())

