from django.db import models
from cart.models import Cart
from Gym_Website.utils import unique_register_id_generator
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from datetime import date, timedelta

User = settings.AUTH_USER_MODEL

class RegisterManager(models.Manager):

    def new_or_get(self, user, cart_obj):
        created = False
        qs = self.get_queryset().filter(user=user, cart=cart_obj, status="Created")

        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(user=user, cart=cart_obj)
            created = True
        return obj, created

    def get_user_registers(self, user):
        active_classes = []
        qs = self.get_queryset().filter(user=user, status="Paid")

        for i in qs:
            if i.expiration_date > date.today():
                active_classes.append(i)

        s = set(active_classes)
        expired_classes = [x for x in qs if x not in s]

        return active_classes, expired_classes


class Register(models.Model):
        class Status(models.TextChoices):
            created = 'Created', "Created"
            paid = 'Paid', "Paid"
            

        user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
        register_id = models.CharField(max_length=120, blank=True)
        cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
        status = models.CharField(max_length=120, default='Created', choices=Status.choices)
        total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
        register_date = models.DateField(blank=True, null=True)
        expiration_date = models.DateField(blank=True, null=True)
        is_expired = models.BooleanField(default=False)

        objects = RegisterManager()

        def __str__(self):
            return self.register_id

        class Meta:
            verbose_name_plural = "Registrations"   

        def update_total(self):
            cart_total = self.cart.total 
            self.total = cart_total
            self.save()
            return cart_total

        def check_done(self):
            user = self.user
            total = self.total
            if user and total > 0:
                return True
            return False

        def mark_paid(self):
            if self.check_done():
                self.status = "Paid"
                self.save()
            return self.status


def add_dates(sender, instance, *args, **kwargs):  
    if instance.status == 'Paid':
        if instance.register_date is None and instance.expiration_date is None:
            instance.register_date = date.today()
            instance.expiration_date = date.today() + timedelta(days=1)
pre_save.connect(add_dates, sender=Register)


def pre_save_create_register_id(sender, instance, *args, **kwargs):
    if not instance.register_id:
        instance.register_id = unique_register_id_generator(instance)
pre_save.connect(pre_save_create_register_id, sender=Register)


def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Register.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            register_obj = qs.first()
            register_obj.update_total()
post_save.connect(post_save_cart_total, sender=Cart)


def post_save_register(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()
post_save.connect(post_save_register, sender=Register)


def change_cart_status(sender, instance, *args, **kwargs):
    if instance.status == "Paid":
        qs = Cart.objects.filter(id=instance.cart.id)
        qs.update(terminated=True)
post_save.connect(change_cart_status, sender=Register)
