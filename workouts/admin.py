from django.contrib import admin
from .models import Workouts, Workout_List
class Workout_ListAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ( 'grade',)
admin.site.register(Workout_List, Workout_ListAdmin)
admin.site.register(Workouts)
