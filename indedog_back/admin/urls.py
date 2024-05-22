from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin),
    path('user/<int:user_id>/', views.user_detail)
]
