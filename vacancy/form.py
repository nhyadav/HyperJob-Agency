from django.forms import ModelForm
from .models import Vacancy

class Vacancyform(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['description']