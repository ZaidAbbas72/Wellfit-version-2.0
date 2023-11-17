from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contact_us.models import Contact_Info, Message
from pages.models import Banner
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from cart.models import Cart
from registers.models import Register
from marketing.models import Marketing

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_again = request.POST['password-again']
        
        if password == password_again:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already associated with an account')
                    return redirect('register')
                else:                
                    user = User.objects.create_user(username=username, first_name=first_name,
                    last_name= last_name,email=email, password=password)
                    user.save()
                    messages.success(request, 'Registration successful. You can now log in')
                    return redirect('login')
        else:
            messages.error(request, 'The entered passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
        
@login_required        
def profile(request):
    banner = Banner.objects.filter(page="profile").first()
    user = request.user
    cart_obj, cart_created = Cart.objects.new_or_get(user)
    register_obj, register_obj_created = Register.objects.new_or_get(user,cart_obj)
    subscribe_obj , created = Marketing.objects.get_or_create(user=user)
    active_registers , expired_registers = Register.objects.get_user_registers(user)

    active_cart_registered=[]
    active_cart_info = []
    active_cart_show = []
    register_id_show = []

    for i in range(len(active_registers)):
        reg_user = active_registers[i]
        active_cart_registered.extend(Cart.objects.registered_carts(reg_user.cart))

    for user,reg_class in zip(active_registers,active_cart_registered):
        register_id_show.append(user.register_id)
            
        if user.cart == reg_class:
            active_cart_info = []
            string_active_cart_info = ""
            for i in reg_class.selected_class.all():    
                active_cart_info.append(i.title)
                string_active_cart_info = str(active_cart_info)
                translation_table = dict.fromkeys(map(ord, '][\''), None)                
                string_active_cart_info = string_active_cart_info.translate(translation_table)

            online_active_cart_info = []
            online_string_active_cart_info = ""
            for i in reg_class.online_selected_class.all():
                online_active_cart_info.append(i.title)
                online_string_active_cart_info = str(online_active_cart_info)
                translation_table = dict.fromkeys(map(ord, '][\''), None)
                online_string_active_cart_info = online_string_active_cart_info.translate(translation_table)

            final_items = online_string_active_cart_info + " , " + string_active_cart_info   
            active_cart_show.append(final_items)
                  
    final_active_list = zip(register_id_show, active_cart_show)


    expired_cart_registered=[]
    expired_cart_info = []
    expired_cart_show = []
    register_id_show = []

    for i in range(len(expired_registers)):
        reg_user = expired_registers[i]
        expired_cart_registered.extend(Cart.objects.registered_carts(reg_user.cart))

    for user,reg_class in zip(expired_registers,expired_cart_registered):
        register_id_show.append(user.register_id)
             
        if user.cart == reg_class:
            expired_cart_info = []
            string_expired_cart_info = ""
            for i in reg_class.selected_class.all():    
                expired_cart_info.append(i.title)
                string_expired_cart_info = str(expired_cart_info)
                translation_table = dict.fromkeys(map(ord, '][\''), None)
                string_expired_cart_info = string_expired_cart_info.translate(translation_table)

            online_expired_cart_info = [] 
            online_string_expired_cart_info = ""
            for i in reg_class.online_selected_class.all():
                online_expired_cart_info.append(i.title)
                online_string_expired_cart_info = str(online_expired_cart_info)
                translation_table = dict.fromkeys(map(ord, '][\''), None)
                online_string_expired_cart_info = online_string_expired_cart_info.translate(translation_table)

            final_items = online_string_expired_cart_info + " , " + string_expired_cart_info   
            expired_cart_show.append(final_items)

    final_expired_list = zip(register_id_show, expired_cart_show)
                   
    if 'submit_changes' in request.POST:
        new_password = request.POST.get("change_password", None)
        if  len(new_password) > 0:
            try:
                validate_password(new_password)
                request.user.password = make_password(new_password, None, 'md5')
                request.user.save()
            except ValidationError:
                messages.error(request, "The entered password is not strong enough")
                
        subscribe_status = request.POST.get("subscribe_checkbox", False)
        if subscribe_status:
            subscribe_obj.subscribed = True
            subscribe_obj.save()
        else:
            subscribe_obj.subscribed = False
            subscribe_obj.save()
        return HttpResponseRedirect(request.path_info)

    if 'checkout' in request.POST:
        is_done = register_obj.check_done()
        if is_done:
            register_obj.mark_paid()
            return redirect("success")

    msg_obj = Message.objects.filter(user=request.user)
    index = len(cart_obj.selected_class.all())
    context = {
        'banner' : banner,
        'index' : index,
        'cart': cart_obj,
        'object':register_obj,
        'active_cart_show' : active_cart_show,
        'expired_cart_show' : expired_cart_show,
        'checked' : subscribe_obj.subscribed,
        'email_messages' : msg_obj,
        'final_expired_list' : final_expired_list,
        'final_active_list' : final_active_list,
    }

    return render(request, 'accounts/profile.html',context)

@login_required
def success(request):
    active_registers , expired_registers = Register.objects.get_user_registers(request.user)

    last_register = active_registers[-1]
    return render(request, 'success-page.html',{'id': last_register.register_id})
