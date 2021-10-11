from django.forms import ModelForm
from .models import Resume

class Resumeform(ModelForm):
    class Meta:
        model = Resume
        fields = ['description']
