from django.urls import path
from . import views
from cart.views import cart_add, profile_registers_api_view,online_cart_add
urlpatterns = [

    path('api/profile',profile_registers_api_view,name='api-profile'),
    path('update',cart_add,name='update'),
    path('update_online',online_cart_add,name='update_online'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('success',views.success,name='success'),
]
