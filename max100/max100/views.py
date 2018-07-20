from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from jwt_auth.mixins import JSONWebTokenAuthMixin
# from max100.models import Game

class GameView(JSONWebTokenAuthMixin, APIView):
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        return Response("GAME")


