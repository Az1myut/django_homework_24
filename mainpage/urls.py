from django.urls import path
from .views import index
app_name='mainpage'
urlpatterns = [
    path('',index,name='index')
]