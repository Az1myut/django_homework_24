from django.shortcuts import render
from .models import Student
app_name='students'
# Create your views here.
def show_students_grid(request):
    students=Student.objects.prefetch_related('on_class')
    template_='show_students_grid.html'
    context={
        'students':students,
    }
    return render(request,template_,context=context)
