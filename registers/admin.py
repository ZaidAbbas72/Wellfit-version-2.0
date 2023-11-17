from django.contrib import admin
from .models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('register_id', 'user', 'is_expired')
    search_fields = ('register_id', 'user__username', 'expiration_date')
    list_filter = ( 'expiration_date', 'is_expired')


admin.site.register(Register, RegisterAdmin)