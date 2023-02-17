from django.shortcuts import render
from teachers.models import Teacher
from subjects.models import Subject

# Create your views here.

def show_mainpage(request):
    template_ = 'mainpage.html'
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers,
    }
    return render(request=request, template_name=template_, context=context)
