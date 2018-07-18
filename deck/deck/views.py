from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from deck.models import Deck

class DeckView(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        deck = Deck()
        deck.shuffle()
        return Response(deck.json_cards())

