from django.urls import path

from teachers.urls import app_name

from .views import SubjectListView, SubjectTemplateView, SubjectAddView,\
        SubjectUptadeView, SubjectDeleteView
# from classboard.views import filter_students_group

app_name = 'subjects'

urlpatterns = [
    path('',SubjectListView.as_view() , name='subjects_view'),
    path('<int:pk>/', SubjectTemplateView.as_view(), name='subjects_view'),
    path('add', SubjectAddView.as_view(), name='subject_add'),
    path('<int:pk>/uptade', SubjectUptadeView.as_view(), name='subject_uptade' ),
    path('<int:pk>/delete', SubjectDeleteView.as_view(), name='subject_delete'),
    # # path('with_teacher/', show_classes_teacher, name='show_classes_teacher'),
    # # path('with_teacher/<int:pk>', show_classes_teacher, name='show_classes_teacher'),
    # # path('with_teacher', class_view, name='class_view'),
    # path('change_teacher/<int:pk>/<int:tpk>', change_teacher, name='change_teacher'),
    # # path('filter_group/', filter_students_group, name='filter_students_group'),
]
