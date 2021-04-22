from django import forms
from django.forms import ModelForm
from .models import Time

class TimeForm(ModelForm):
    time = forms.TimeField(label='Time: (HH:MM:SS.ssssss)', widget=forms.TimeInput(format='%H:%M:%S.%f'))
    class Meta:
        model = Time
        fields = ['date', 'time']