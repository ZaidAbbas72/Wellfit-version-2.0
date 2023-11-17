from django.db import models
from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_id = models.CharField(max_length=20)  # YouTube video ID

    def __str__(self):
        return self.title

# Create your models here.
