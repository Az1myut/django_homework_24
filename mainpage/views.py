from django.shortcuts import render
from teachers.models import Teacher
from subjects.models import Subject

from icecream import ic

# Create your views here.

def show_mainpage(request):
    template_ = 'mainpage.html'
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()

    # ic(teachers.subject)
    context = {
        'teachers': teachers,
        'subjects': subjects,
    }
    return render(request=request, template_name=template_, context=context)
