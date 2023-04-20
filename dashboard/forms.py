from django.forms import ModelForm
from .models import Opexseoul

class OpexseoulForm(ModelForm) :
    class Meta : 
        model = Opexseoul
        fields = '__all__'