from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# from max100.models import Game

class GameView(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        return Response("GAME")


