from django.shortcuts import render, get_object_or_404
from .models import Class, PublicOnlineClass, PrivateOnlineClass
from contact_us.models import Contact_Info
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from pages.models import Banner
from cart.models import Cart
from registers.models import Register

def presence_classes(request):
    classes = Class.objects.filter(is_published=True).order_by('id')
    paginator = Paginator(classes,6)    
    page = request.GET.get('page')
    paged_classes = paginator.get_page(page)
    banner = Banner.objects.filter(page="presence_class").first()
    context = {
        'classes' : paged_classes,
        'banner' : banner,

    }
    
    cart_registered = []
    cart_items = []
    user = request.user

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


    return render(request, './classes/presence-classes.html',context)


def private_classes(request):
    classes = PrivateOnlineClass.objects.filter(is_published=True).order_by('id')
    paginator = Paginator(classes,6)    
    page = request.GET.get('page')
    paged_classes = paginator.get_page(page)
    banner = Banner.objects.filter(page="online_private_class").first()
    context = {
        'classes' : paged_classes,
        'banner' : banner,

    }
    
    cart_registered = []
    cart_items = []
    user = request.user

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
                for i in reg_class.online_selected_class.all():    
                    active_cart_info.append(i.title)

        context.update({'cart_items' : active_cart_info})

    return render(request, './classes/private-classes.html',context)


def public_classes(request):
    classes = PublicOnlineClass.objects.filter(is_published=True).order_by('id')
    paginator = Paginator(classes,6)    
    page = request.GET.get('page')
    paged_classes = paginator.get_page(page)
    banner = Banner.objects.filter(page="online_public_class").first()
    context = {
        'classes' : paged_classes,
        'banner' : banner,
    }
    
  
    return render(request, './classes/public-classes.html',context)

def class_details(request,class_id):
    details = get_object_or_404(Class, pk=class_id)
    classes = Class.objects.filter(is_published=True)
    banner = Banner.objects.filter(page="presence_class_details").first()
    context = {
        'classes' : classes,
        'details' : details,
        'banner' : banner,
        'class1' : classes[0],
        }
    return render(request, './classes/class-details.html',context)



def private_class_details(request,class_id):
    details = get_object_or_404(PrivateOnlineClass, pk=class_id)
    classes = PrivateOnlineClass.objects.filter(is_published=True)
    banner = Banner.objects.filter(page="online_private_class_details").first()
    context = {
        'classes' : classes,
        'details' : details,
        'banner' : banner,
        'class1' : classes[0],
        }

    cart_registered = []
    cart_items = []
    user = request.user

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
                for i in reg_class.online_selected_class.all():    
                    active_cart_info.append(i.title)

        context.update({'cart_items' : active_cart_info})
    return render(request, './classes/private-online-class-details.html',context)




def public_class_details(request,class_id):
    details = get_object_or_404(PublicOnlineClass, pk=class_id)
    classes = PublicOnlineClass.objects.filter(is_published=True)
    banner = Banner.objects.filter(page="online_public_class_details").first()
    context = {
        'classes' : classes,
        'details' : details,
        'banner' : banner,
        'class1' : classes[0],
        }
    return render(request, './classes/public-online-class-details.html',context)