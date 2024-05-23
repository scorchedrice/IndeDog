from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework import status

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Article, Comment, Mozip
from movies.models import Movie, Cinema
from .serializers import ArticleSerializer, CommentSerializer, CommentMovieSerializer, ArticleLikeSerializer, CommentCinemaSerializer, JobSerializer, JobSubmitSerializer, JobUpdateSerializer


# Create your views here.
@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create_article(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        serializer = CommentMovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def notice(request):
    if request.method == 'GET':    
        articles = Article.objects.filter(is_notice=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, is_notice=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_movie(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    if request.method == 'PUT':
        serializer = CommentMovieSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def article_like(request, article_pk):
    article = Article.objects.prefetch_related('like_users').get(pk=article_pk)
    serializer = ArticleLikeSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_create_cinema(request, cinema_name):
    cinema = Cinema.objects.get(address=cinema_name)
    if request.method == 'POST':
        serializer = CommentMovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, cinema=cinema)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def job_create(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def job(request):
    if request.method == 'GET':
        jobs = Mozip.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def job_detail(request, job_pk):
    if request.method == 'GET':
        job = Mozip.objects.prefetch_related('applicant').get(pk=job_pk)
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def job_submit(request, job_pk):
    job = Mozip.objects.prefetch_related('applicant').get(pk=job_pk)
    
    if request.method == 'PUT':
        serializer = JobSubmitSerializer(job, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def job_article_update(request, job_pk):
    job = Mozip.objects.get(pk=job_pk)
    if request.method == 'PUT':
        serializer = JobUpdateSerializer(job, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
