from django.forms import ModelForm
from .models import Magazine

class ManazineForm(ModelForm):
    class Meta:
        model = Magazine
        fields = ('title', 'content')
