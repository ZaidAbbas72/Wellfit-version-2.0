from django.contrib import admin
from .models import Banner, CarouselBanner, Honors


class BannerAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects > 12:
      return False
    else:
      return True

admin.site.register(Banner, BannerAdmin)
admin.site.register(CarouselBanner)
admin.site.register(Honors)