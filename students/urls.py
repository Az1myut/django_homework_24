from django.urls import path
from .views import (
    StudentAddView,
    StudentTempateView,
    StudentDeleteView,
    StudentUpdateView,
    StudentListView,

    GroupListView,
    GroupTemplateView,
    GroupAddView,
    GroupDeleteView,
    GroupUpdateView
)


urlpatterns = [
    path("", StudentListView.as_view(), name="students_view"),
    path("<int:pk>/", StudentTempateView.as_view(), name="students_view"),
    path("add", StudentAddView.as_view(), name="student_add"),
    path("<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),
    path("<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),

    path('groups/', GroupListView.as_view(), name='groups_view'),
    path('groups/<int:pk>', GroupTemplateView.as_view(), name='groups_view'),
    path("groups/add", GroupAddView.as_view(), name="group_add"),
    path("groups/<int:pk>/delete/", GroupDeleteView.as_view(), name="group_delete"),
    path("groups/<int:pk>/update/", GroupUpdateView.as_view(), name="group_uptade"),
]
