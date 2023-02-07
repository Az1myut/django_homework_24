from django.urls import path
from .views import classboard_view,classboard_week_view

urlpatterns = [
    path('', classboard_view, name='classboard_view'),
    path('<int:pk>', classboard_view, name='classboard_view'),  
    path('week',classboard_week_view,name='classboard_week_view') 
]
