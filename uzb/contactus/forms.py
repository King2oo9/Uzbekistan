from django.forms import ModelForm
from .models import Contact


class Cnt(ModelForm):
    class Meta:
        model = Contact
        fields = ['ism', 'mavzu', 'matn']
