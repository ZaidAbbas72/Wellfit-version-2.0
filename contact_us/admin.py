from django.contrib import admin
from .models import Contact_Info, Message

class Contact_InfoAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(Contact_Info, Contact_InfoAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_guest')
    list_filter = ( 'is_guest',)

admin.site.register(Message, MessageAdmin)