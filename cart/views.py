from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from classes.models import Class, PrivateOnlineClass
from .models import Cart
from django.shortcuts import render
from registers.models import Register


def profile_registers_api_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request.user)
    classes = []
    presence_classes = [{"id": x.id,
                "title": x.title,
                "price": x.price,
                } for x in cart_obj.selected_class.all()]
    
    online_classes = [{"id": x.id,
                "title": x.title,
                "price": x.price,
                } for x in cart_obj.online_selected_class.all()]
    classes.append(presence_classes + online_classes)
   

    cart_data = {"classes": classes, "total": cart_obj.total}
    return JsonResponse(cart_data)


def cart_add(request):
    class_id = request.POST.get('class_id')
    if class_id is not None:
        try:
            class_obj = Class.objects.get(id=class_id)
        except:
            return redirect('index')

        user = request.user
        if user.is_authenticated:
            
            active_registers , expired_registers = Register.objects.get_user_registers(user)
            active_cart_registered=[]
            active_cart_info = []

            for i in range(len(active_registers)):
                reg_user = active_registers[i]
                active_cart_registered.extend(Cart.objects.registered_carts(reg_user.cart))

            for reg_class in active_cart_registered:
                    for i in reg_class.selected_class.all():    
                        active_cart_info.append(i.title)
    
            cart_obj, new_obj = Cart.objects.new_or_get(user)

            if class_obj in cart_obj.selected_class.all() and class_obj.title not in active_cart_info:
                cart_obj.selected_class.remove(class_obj)
                added = False
            elif class_obj not in cart_obj.selected_class.all() and class_obj.title not in active_cart_info:
                cart_obj.selected_class.add(class_obj)
                added = True

        if request.is_ajax:
            json_data = {
                    "added": added,
                    "removed": not added,
                    "cartItemCount" : cart_obj.selected_class.count() + cart_obj.online_selected_class.count(),
            }
            return JsonResponse(json_data)
    return redirect('profile')


def online_cart_add(request):
    class_id = request.POST.get('online_class_id')
    if class_id is not None:
        try:
            class_obj = PrivateOnlineClass.objects.get(id=class_id)
        except:
            return redirect('index')

        user = request.user
        if user.is_authenticated:

            
            active_registers , expired_registers = Register.objects.get_user_registers(user)
            active_cart_registered=[]
            active_cart_info = []

            for i in range(len(active_registers)):
                reg_user = active_registers[i]
                active_cart_registered.extend(Cart.objects.registered_carts(reg_user.cart))

            for reg_class in active_cart_registered:
                    for i in reg_class.online_selected_class.all():    
                        active_cart_info.append(i.title)
    
            cart_obj, new_obj = Cart.objects.new_or_get(user)
            if cart_obj.online_selected_class not in active_cart_info:

                
                if class_obj in cart_obj.online_selected_class.all():
                    cart_obj.online_selected_class.remove(class_obj)
                    added = False
                else:
                    cart_obj.online_selected_class.add(class_obj)
                    added = True

        if request.is_ajax:
            json_data = {
                    "added": added,
                    "removed": not added,
                    "cartItemCount" : cart_obj.selected_class.count() + cart_obj.online_selected_class.count(),
            }
            return JsonResponse(json_data)
    return redirect('profile')


