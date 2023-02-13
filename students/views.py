from tempfile import template
from tokenize import group
from django.shortcuts import render,get_object_or_404
from django.template import context
from .models import Group, Student
from icecream import ic
# Create your views here.

def show_students_grid(request,pk=None)->render:
    if not pk:
        groups=Group.objects.all()
        main_list=[]
       
        maxx=0
        for group in groups:
            students=group.student_group.all()
            if len(students)>maxx:
                maxx=len(students)


        for group in groups:
            students=group.student_group.all()
            students=list(students)
            if len(students)<maxx:
                for i in range(maxx-len(students)):
                    students.append('')
            group_name=students[0].group
            students.insert(0,group_name)
            main_list.append(students)
        ic(groups[1].student_group.all())
        context={
            'groups':groups,
            'main_list':main_list,
            
            
        }
        template_='students_all.html'

    else:
        current_student=get_object_or_404(Student,pk=pk)
        template_='students_detail.html'
        context={
            'current_student' : current_student,
        }
    return render(request,template_,context=context)
