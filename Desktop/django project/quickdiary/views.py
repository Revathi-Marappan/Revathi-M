from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def homepage(request):
    return render (request,'index.html')



def mood_tracker_list(request):
    if request.method =='POST':
        name=request.POST.get('name')
        name=request.POST.get('date')   
        name=request.POST.get('time')
        name=request.POST.get('mood')   
        name=request.POST.get('mood_intensity')   
        name=request.POST.get('performance')   
        name=request.POST.get('performance_score')   
        name=request.POST.get('stress_level')   
        name=request.POST.get('energy_level')   
        name=request.POST.get('physical_health')   
        name=request.POST.get('activities')   
        name=request.POST.get('social_interaction')   
        name=request.POST.get('weather')   
        name=request.POST.get('mental_clarity')   
        name=request.POST.get('gratitude')   
        name=request.POST.get('self_care')
        MoodTracker.objects.create