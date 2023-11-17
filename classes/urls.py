from . import views
from django.urls import path

urlpatterns = [
    path('presence_classes', views.presence_classes, name='presence_classes'),
    path('presence_classes/<int:class_id>', views.class_details, name='class_details'),
    path('private_classes', views.private_classes, name='private_classes'),
    path('private_classes/<int:class_id>', views.private_class_details, name='private_class_details'),
    path('public_classes', views.public_classes, name='public_classes'),
    path('public_classes/<int:class_id>', views.public_class_details, name='public_class_details'),
]
