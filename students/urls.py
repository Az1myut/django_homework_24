from django.urls import path
from .views import show_students_grid
app_name='students'
urlpatterns = [
    path('',show_students_grid,name='show_students_grid'),
    path('<int:pk>',show_students_grid,name='show_students_grid')
]