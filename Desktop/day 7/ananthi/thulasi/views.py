from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def homepage(request):
    return render (request,'index.html')




    def student_form(request):
        if request.method =='POST':
            name=request.POST.get('name')
            roll_no=request.POST.get('roll_no')
            email=request.POST.get('email')
            student.objects.create(name=name,roll_no=roll_no,email=email)
            return redirect('student_form')
        students=student.object.all()
        return render(request,'index.html',{'students':students})