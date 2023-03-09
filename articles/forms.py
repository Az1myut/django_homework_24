from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'image', 'author')
        labels = {
            'title': 'Название',
            'text': 'Текст',
            'image': 'Изображение',
            'author': 'Автор',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('text', )
        labels = {
            'text': 'Комментарий',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }