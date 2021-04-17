from django.forms import ModelForm
from .models import Time

class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = ['date', 'time']