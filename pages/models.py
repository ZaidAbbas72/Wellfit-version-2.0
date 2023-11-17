from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

    
class CarouselBanner(models.Model):
     image = models.ImageField(upload_to='banners/carousel_banners/%Y/%m/%d')
     small_title = models.CharField(max_length=100, blank=True)
     normal_title_1 = models.CharField(max_length=100, blank=True)
     normal_title_2 = models.CharField(max_length=100, blank=True)
     normal_title_3 = models.CharField(max_length=100, blank=True)
     highlighted_title_1 = models.CharField(max_length=100, blank=True)
     highlighted_title_2 = models.CharField(max_length=100, blank=True)   
     highlighted_title_3 = models.CharField(max_length=100, blank=True)

     def __str__(self):
        return str(self.id)
     class Meta:
        verbose_name_plural = "Home Banners"  


class Banner(models.Model):
    class Pages(models.TextChoices):
            page_1 = 'presence_class', "In-Person Classes"
            page_2 = 'online_private_class', "Online Private Classes"
            page_3 = 'online_public_class', "Online Public Classes"
            page_4  = 'beginner_workouts', "Beginner Workouts"
            page_5 = 'intermediate_workouts', "Intermediate Workouts"
            page_6 = 'advanced_workouts', "Advanced Workouts"
            page_7 = 'our_team', "Our Team"
            page_8 = 'gallery', "Gallery"
            page_9 = 'contact_us', "Contact Us"
            page_10 = 'profile', "Profile"
            page_11 = 'online_private_class_details', "Online Private Class Details"
            page_12 = 'online_public_class_details',"Online Public Class Details"
            page_13 = 'presence_class_details',"In-Person Class Details"
                
    image = models.ImageField(upload_to='banners/pages_banners/%Y/%m/%d')
    title = models.CharField(max_length=100)
    page = models.CharField(max_length=100, choices=Pages.choices, unique=True)
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = "Banners"     


class Honors(models.Model):
    image = models.ImageField(upload_to='honors/%Y/%m/%d')
    description = models.TextField()
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = "Club Honors"     
