from django.db import models
from classes.models import Class, PrivateOnlineClass
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed
import registers

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def registered_carts(self, cart):
        qs = self.get_queryset().filter(id=cart.id)
        if qs.exists():
            cart_obj = qs.all()
            return cart_obj

    def new_or_get(self, user):
        qs = self.get_queryset().filter(user=user, terminated=False)
        if qs.exists():
            new_obj = False
            cart_obj = qs.first()
        else:
            cart_obj = self.model.objects.create(user=user)
            new_obj = True
        return cart_obj, new_obj

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    selected_class = models.ManyToManyField(Class, blank=True)
    online_selected_class = models.ManyToManyField(PrivateOnlineClass, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    terminated = models.BooleanField(default=False)

    objects = CartManager()

    def __str__(self):
        return "Request #" + str(self.id)

    class Meta:
        verbose_name_plural = "Requested Classes for Registration"

def m2m_changed_presence_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        selected_class = instance.selected_class.all()
        online_selected_class = instance.online_selected_class.all()
        total = 0
        for x in selected_class:
            total += x.price
        for y in online_selected_class:
            total += y.price
        instance.total = total
        instance.save()

m2m_changed.connect(m2m_changed_presence_receiver, sender=Cart.selected_class.through)

def m2m_changed_online_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        selected_class = instance.selected_class.all()
        online_selected_class = instance.online_selected_class.all()
        total = 0
        for x in selected_class:
            total += x.price
        for y in online_selected_class:
            total += y.price
        instance.total = total
        instance.save()

m2m_changed.connect(m2m_changed_online_receiver, sender=Cart.online_selected_class.through)
