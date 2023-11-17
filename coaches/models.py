from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Coach(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='coaches/%Y/%m/%d')
    live_stream_link = models.URLField(blank=True, null=True)
    classes = models.TextField(blank=True)   
    info_1 = models.CharField(max_length=200,blank=True)
    info_2 = models.CharField(max_length=200,blank=True)
    info_3 = models.CharField(max_length=200,blank=True)
    info_4 = models.CharField(max_length=200,blank=True)
    hire_date = models.DateField(default=datetime.now,blank=False)
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Coaches"





