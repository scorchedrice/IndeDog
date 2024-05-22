from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework import status

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model  
from .serializers import UserSerializer

# Create your views here.

user = get_user_model()

@api_view(['GET'])
def admin(request):
    if request.method == 'GET':
        # users = get_user_model().objects.all()
        users = user.objects.prefetch_related('like_movies')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_detail(request, user_id):
    if request.method == 'GET':
        user = get_user_model().objects.prefetch_related('like_movies').get(pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
