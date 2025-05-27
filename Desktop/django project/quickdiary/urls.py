from django.urls import path
from . import *

urlpatterns = [
    path('home/',homepage),
    path('MoodTracker/', MoodTracker, name='MoodTracker'),
]                