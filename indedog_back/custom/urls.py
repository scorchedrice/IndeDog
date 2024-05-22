from django.urls import path
from . import views

urlpatterns = [
    path('', views.user),
    path('user/<str:username>/', views.user_detail),
    path('avatar/create/', views.user_avatar_create),
]
