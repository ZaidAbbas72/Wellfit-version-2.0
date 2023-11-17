from django.shortcuts import render, get_object_or_404
from .models import Workout_List, Workouts
from contact_us.models import Contact_Info
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pages.models import Banner

def beginner_workouts_list(request):
    workouts = Workout_List.objects.filter(is_published=True,grade="مبتدی")
    paginator = Paginator(workouts,6)  
    page = request.GET.get('page')
    paged_workouts = paginator.get_page(page)
    banner = Banner.objects.filter(page="beginner_workouts").first()
    context = {
        'workouts' : paged_workouts,
        'banner' : banner,
    }
    return render(request, './workouts/beginner-workouts.html',context)


def intermediate_workouts_list(request):
    workouts = Workout_List.objects.filter(is_published=True,grade="متوسط")
    paginator = Paginator(workouts,6)  
    page = request.GET.get('page')
    paged_workouts = paginator.get_page(page)
    banner = Banner.objects.filter(page="intermediate_workouts").first()
    context = {
        'workouts' : paged_workouts,
        'banner' : banner,
    }    
    return render(request, './workouts/intermediate-workouts.html',context)

def advanced_workouts_list(request):
    workouts = Workout_List.objects.filter(is_published=True,grade="پیشرفته")
    paginator = Paginator(workouts,6)  
    page = request.GET.get('page')
    paged_workouts = paginator.get_page(page)
    banner = Banner.objects.filter(page="advanced_workouts").first()
    context = {
        'workouts' : paged_workouts,
        'banner' : banner,
    }
    return render(request, './workouts/advanced-workouts.html',context)

def search(request):
    workouts = Workout_List.objects.filter(is_published=True)
    beginner_workouts = Workout_List.objects.filter(is_published=True,grade="مبتدی")
    intermediate_workouts = Workout_List.objects.filter(is_published=True,grade="متوسط")
    advanced_workouts = Workout_List.objects.filter(is_published=True,grade="پیشرفته")
    queryset_list_woekouts = Workouts.objects.all()
    banner = Banner.objects.filter(page="beginner_workouts").first()
    queryset_list = []
    beginner_query = []
    intermediate_query = []
    advanced_query = []

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list.extend(queryset_list_woekouts.filter(title__icontains=keywords))

    if 'workouts-list' in request.GET:
        workouts_list = request.GET['workouts-list']
        search_workouts = Workout_List.objects.filter(title=workouts_list)
        if workouts_list:
            for i in search_workouts:         
                queryset_list.extend(i.selected_workouts.all())


    if 'beginner' in request.GET:
        display_type = request.GET.get("beginner", None)
        for i in beginner_workouts:
             beginner_query.extend(i.selected_workouts.all())
        if display_type == "beginner":
            [queryset_list.append(x) for x in beginner_query if x not in queryset_list] 
        


    if 'intermediate' in request.GET:
        display_type = request.GET.get("intermediate", None)
        for i in intermediate_workouts:
            intermediate_query.extend(i.selected_workouts.all())
        if display_type == "intermediate":
            [queryset_list.append(x) for x in intermediate_query if x not in queryset_list]

    if 'advanced' in request.GET:
        display_type = request.GET.get("advanced", None)
        for i in advanced_workouts:
            advanced_query.extend(i.selected_workouts.all())
        if display_type == "advanced":
            [queryset_list.append(x) for x in advanced_query if x not in queryset_list]

    context = {
        'workouts' : workouts,
        'queryset_list' : queryset_list,
        'banner' : banner,
    }
    return render(request, './workouts/search.html',context)


def workouts(request,workout_id):
    workouts = get_object_or_404(Workout_List, pk=workout_id)
    context = {
        'workouts' : workouts,
        }
    return render(request, './workouts/workouts.html',context)