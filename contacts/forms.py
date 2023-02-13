from dataclasses import field, fields
from django import forms
from .models import ContactMessage
from django.core.exceptions import ValidationError
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ("subject", "first_name", "last_name", "email", "phone" , "message")
        # widgets = {

        # }
        # widjets = widgets = {'subject' : forms.IntegerField(help_text='Введите тему сообщения', label= 'Тема Сообщения',
        #                     required=True),'attrs' : ['class', 'form-control']
        # }
       