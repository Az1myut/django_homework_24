from tempfile import template
from unittest import removeResult
from django.shortcuts import render
from django.template import context
from teachers.models import Teacher
from classes.models import Class
# Create your views here.

def index(request)->render:
    teachers=Teacher.objects.all()
    subjects=Class.objects.all()
    context={
        'teachers':teachers,
        'subjects':subjects,
    }
    template_='mainpage.html'
    return render(request,template_,context)