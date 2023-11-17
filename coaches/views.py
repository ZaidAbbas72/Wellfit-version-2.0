from django.shortcuts import render
from .models import Coach
from pages.models import Banner
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from classes.models import Class, PrivateOnlineClass, PublicOnlineClass

def our_team(request):
    banner = Banner.objects.filter(page="our_team").first()
    coaches = Coach.objects.all()
    paginator = Paginator(coaches,6)    
    page = request.GET.get('page')
    paged_coaches = paginator.get_page(page)

    
       
    context = {
        'banner' : banner,
        'coaches' : paged_coaches,
    }
    return render(request, './our_team.html',context)
