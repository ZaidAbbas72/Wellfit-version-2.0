from django.contrib import messages
from datetime import date
from contact_us.models import Contact_Info
from marketing.utils import Mailchimp
from marketing.models import Marketing, GuestMarketing
from cart.models import Cart
from registers.models import Register
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

def info(request):
    info = Contact_Info.objects.all()
    if 'submit_footer_subscribe' in request.POST:    
        subscribe_email = request.POST.get('email_subscribe', None)
        if len(subscribe_email) != 0:
            email = Marketing.objects.filter(user__email=subscribe_email).first()
            if email is not None:
                if subscribe_email != email.user.email: 
                    guest_email, guest_created = GuestMarketing.objects.get_or_create(guest_email=subscribe_email)
                    if guest_created:
                        Mailchimp().add_email(subscribe_email)
                        messages.success(request, 'Your email has been successfully registered')                
                else:   
                    messages.error(request, 'Your email is already registered')
            else:
                guest_email, guest_created = GuestMarketing.objects.get_or_create(guest_email=subscribe_email)
                if guest_created:
                    Mailchimp().add_email(subscribe_email)
                    messages.success(request, 'Your email has been successfully registered')                
                else:   
                    messages.error(request, 'Your email is already registered')
                    
    context = {
        'info' : info.first(),  
    }

    all_users = User.objects.all()
    for user in all_users:
        active_registers , expired_registers = Register.objects.get_user_registers(user)
        for i in expired_registers:
            i.is_expired=True
            i.save()
        
    if request.user.is_authenticated:
        cart_obj, new_obj = Cart.objects.new_or_get(request.user)
        cart_count = cart_obj.selected_class.count() + cart_obj.online_selected_class.count()
        context.update({'cart_count' : cart_count})
        
    return(context)
