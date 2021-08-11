from django import forms

from .models import NewsLetterModel


class NewsLetterModelForm(forms.ModelForm):
    class Meta:
        model = NewsLetterModel
        fields = ['email']
        labels = {'Email': ''}