from django.shortcuts import render
from django.core.mail import send_mail
from .models import Contact_Info, Message
from pages.models import Banner
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def contact_us(request):
    banner = Banner.objects.filter(page="contact_us").first()
    info = Contact_Info.objects.all()
    if request.POST.get('submit'):
        message_content = request.POST['message-content']
        full_name = request.POST['full-name']
        email = request.POST['email']
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        admin_emails = []
        msg_obj = Message.objects.get_or_create(full_name=full_name, email=email, message=message_content, user=user)
        admin_user = User.objects.filter(is_superuser=True)
        for i in admin_user:
            admin_emails.append(i.email)
        
        send_mail(
            'User Message from Website',
            'Username: ' + full_name + '\n' + 'Email: ' + email + '\n\n\n' + message_content,
            email,
            admin_emails,
            fail_silently=False,
        )   
        return HttpResponseRedirect(request.path_info)
    context = {
        'banner': banner,
        'informations': info.first(),
    }

    return render(request, './contact_us.html', context)
