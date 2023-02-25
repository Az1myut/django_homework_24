from django.urls import path
from .views import view_teachers, TeacherCreateView, TeacherDeleteView, TeacherUpdateView

app_name = 'teachers'

urlpatterns = [
    path('', view_teachers, name='view_teachers'),
    path('<int:pk>/', view_teachers, name='view_teacher'),
    path('create/', TeacherCreateView.as_view(), name='create_teachers'),
    path('<int:pk>/update',TeacherUpdateView.as_view(),name='update_teachers'),
    path('<int:pk>/delete',TeacherDeleteView.as_view(), name='delete_teachers')


]