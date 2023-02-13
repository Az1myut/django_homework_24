from unicodedata import name
from django.urls import path 
from .views import contact_info, contact_message
app_name = 'contacts'
urlpatterns = [
    path('', contact_info , name='contact_info' ),
    path('forms_check',contact_message, name='contact_message')
]