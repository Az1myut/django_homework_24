from django.urls import path
from wages.views import show_teachers_grid, wage_recalculate

app_name = 'wages'

urlpatterns = [
    path('', show_teachers_grid, name='show_teachers_grid'),
    #show  wages of teachers by filter(some conditions)
    path('<int:pk>/', show_teachers_grid, name='show_teachers_grid'),
    #show wage of exact teacher by its pk
    path('recalculate/<int:pk>/', wage_recalculate, name='wage_recalculate'),
    #show how wages were recalcilated
]
