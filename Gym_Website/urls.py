from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorials/', include('video_tutorials.urls')),
    path('gallery/', include('gallery.urls')),
    path('our_team/', include('coaches.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('classes/', include('classes.urls')),
    path('accounts/', include('accounts.urls')),
    path('workouts/', include('workouts.urls')),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

