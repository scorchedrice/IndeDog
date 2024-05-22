from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('create/', views.article_create),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/like/', views.article_like),
    path('<int:article_pk>/update/', views.article_update),
    path('<int:article_pk>/comments/', views.comment_create_article),
    path('movie/<int:movie_pk>/comments/', views.comment_create_movie),
    path('movie/<int:comment_pk>/comments/update/', views.comment_update_movie),
    path('notices/', views.notice),
]
