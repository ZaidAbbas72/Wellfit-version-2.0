from django.urls import path
from . import views
from .context_processors import info

urlpatterns = [
    path('', views.index, name='index'),
]