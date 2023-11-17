from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorial_list, name='tutorial_list'),
    path('tutorial/<str:video_id>/', views.tutorial_detail, name='tutorial_detail'),
]
