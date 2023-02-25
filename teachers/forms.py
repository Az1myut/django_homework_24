from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Фамилия'
            }),
            'phone': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Телефон'
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'image': forms.FileInput(attrs={'class': 'img-fluid'}),

            'oubject': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'max-width: 300px;'})
        }  