from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/like/', views.movie_like),
    path('cinemas/', views.cinema_list),
]
