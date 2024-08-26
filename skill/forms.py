from django import forms
from django.utils import timezone

class cform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField()
    time = forms.DateTimeField(initial=timezone.now)