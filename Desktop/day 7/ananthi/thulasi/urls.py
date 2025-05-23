from django.urls import path
from .views import *


urlpatterns=[
    path('home/',homepage),
    path('student_form/', student_form, name='student_form'), # Add a name here
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    ]
 