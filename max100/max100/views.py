from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from jwt_auth.mixins import JSONWebTokenAuthMixin
from max100.models import Max100

class GameView(JSONWebTokenAuthMixin, APIView):
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        game = Max100()
        game.new_deck()
        if game.draw_pile:
            return Response("New game started.")
        else:
            return Response("Something went wrong.")

