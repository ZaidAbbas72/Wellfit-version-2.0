from django.contrib import admin
from .models import Class, PrivateOnlineClass, PublicOnlineClass

admin.site.register(Class)
admin.site.register(PrivateOnlineClass)
admin.site.register(PublicOnlineClass)

