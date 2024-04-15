from django import forms
from .models import Musicas, Bandas, Albuns

class MusicasForm(forms.ModelForm):
    class Meta:
        model = Musicas
        fields = '__all__'
        
    # class Meta:
    #     model = Bandas
    #     fields = '__all__'
    # class Meta:
    #     model = Albuns
    #     fields = '__all__'
    
# class AlbunsForm(forms.ModelForm):
#     class Meta:
#         model = Albuns
#         fields = '__all__'
# class BandasForm(forms.ModelForm):
#     class Meta:
#         model = Bandas
#         fields = '__all__'