from django.forms import ModelForm
from .models import Quot


class DataForm(ModelForm):
    class Meta:
        model = Quot
        fields = ['category', 'quantity']