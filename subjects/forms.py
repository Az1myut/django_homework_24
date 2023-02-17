from django import forms
from .models import Subject
class SubjectAddForm(forms.ModelForm):
  

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Subject
        fields = ('name',)
