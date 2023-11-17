from django.urls import path
from . import views

urlpatterns = [

    path('', views.our_team, name='our_team'),

]