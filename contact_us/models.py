from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

class Contact_Info(models.Model):
    address = models.TextField()
    phone = PhoneNumberField(null=False, blank=False)
    email = models.EmailField()
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    bio = models.TextField()

    class Meta:
        verbose_name_plural = "Website Information"

    def __str__(self):
        return "Site Information"


class Message(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
    is_guest = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Messages"


def check_if_guest(sender, instance, *args, **kwargs):
    if instance.user is None:
        instance.is_guest = True
    else:
        instance.is_guest = False

pre_save.connect(check_if_guest, sender=Message)
