from django.db import models
from classes.models import Class

class Gallery(models.Model): 

    FILTER_CHOICES = [
        ("buffet", "Buffet"), 
        ("gym", "Gym Environment"), 
    ]

    classes = Class.objects.all()
    for i in classes:
        FILTER_CHOICES.append((str(i.title), str(i.title)))

    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/%Y/%m/%d')
    display_filter_id = models.CharField(choices=FILTER_CHOICES, max_length=200)

    def __str__(self):
        if not self.title:
            return str("Image Number " + str(self.id))
        else:
            return self.title 

    class Meta:
        verbose_name_plural = "Images"
