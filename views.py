from django.http import JsonResponse
from .models import Games
from .serializers import GamesSerializer

def games_list(request):

    Games.objects.all()
    serializer = GamesSerializer(games, many=True)
    return JsonResponse(serializer.data)