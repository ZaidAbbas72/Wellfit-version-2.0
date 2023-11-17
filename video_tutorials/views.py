from django.shortcuts import render
from django.shortcuts import render
from .models import Tutorial

def tutorial_list(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'video_tutorials/tutorial_list.html', {'tutorials': tutorials})

def tutorial_detail(request, video_id):
    tutorial = Tutorial.objects.get(video_id=video_id)
    return render(request, 'video_tutorials/tutorial_detail.html', {'tutorial': tutorial})

# Create your views here.
