from django.urls import path
from .views import classboard_view, ShowWeekClassboardView

urlpatterns = [
    path('', classboard_view, name='classboard_view'),
    path('<int:pk>', classboard_view, name='classboard_view'),   
    path('week',ShowWeekClassboardView.as_view(), name='classboard_week')
]
