from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):

    

    class Meta:
        model = Pessoa
        fields = '__all__'


    widgets = {
        'date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
    }
       
