from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, CinemaListSerializer, MovieLikeSerializer
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
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    movie = Movie.objects.prefetch_related('like_users').get(pk=movie_pk)
    serializer = MovieLikeSerializer(movie, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)