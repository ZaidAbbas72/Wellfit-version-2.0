from . import views
from django.urls import path

urlpatterns = [

    path('beginner_workouts', views.beginner_workouts_list, name='beginner_workouts'),
    path('intermediate_workouts', views.intermediate_workouts_list, name='intermediate_workouts'),
    path('advanced_workouts', views.advanced_workouts_list, name='advanced_workouts'),
    path('search', views.search, name='search'),
    path('workouts/<int:workout_id>', views.workouts, name='workouts'),

]
