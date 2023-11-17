from django.shortcuts import render, redirect
from classes.models import Class, PublicOnlineClass, PrivateOnlineClass
from gallery.models import Gallery
from coaches.models import Coach
from .models import CarouselBanner, Honors
from cart.models import Cart
from registers.models import Register



def index(request):
    banners = CarouselBanner.objects.all()
    classes = Class.objects.filter(is_published=True).order_by('id')[:3]
    public_online_classes = PublicOnlineClass.objects.filter(is_published=True).order_by('id')[:3]
    private_online_classes = PrivateOnlineClass.objects.filter(is_published=True).order_by('id')[:3]
    gallery = Gallery.objects.all()[:7]
    coaches = Coach.objects.all()[:6]
    honor = Honors.objects.all()

    cart_registered = []
    cart_items = []
    user = request.user
    context = {
        'honors' : honor,
        'banners' : banners,
        'classes' : classes,
        'public_online_classes' : public_online_classes,
        'private_online_classes' : private_online_classes,
        'gallery' : gallery,
        'coaches' : coaches,
        
    }
    if user.is_authenticated :
        cart_obj, cart_created = Cart.objects.new_or_get(user)
        context.update({'cart' : cart_obj})
        active_registers , expired_registers = Register.objects.get_user_registers(user)

        active_cart_registered=[]
        active_cart_info = []

        for i in range(len(active_registers)):
            reg_user = active_registers[i]
            active_cart_registered.extend(Cart.objects.registered_carts(reg_user.cart))

        for reg_class in active_cart_registered:
                for i in reg_class.selected_class.all():    
                    active_cart_info.append(i.title)
        context.update({'cart_items' : active_cart_info})
        
    return render(request, 'index.html',context)



    