from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, CinemaListSerializer
from .models import Movie, Cinema


# Create your views here.
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def cinema_list(request):
    if request.method == 'GET':
        cinemas = get_list_or_404(Cinema)
        serializer = CinemaListSerializer(cinemas, many=True)
        return Response(serializer.data)