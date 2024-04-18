from django import forms
from .models import Musicas

class MusicasForm(forms.ModelForm):
    class Meta:
        model = Musicas
        fields = '__all__'