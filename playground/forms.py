from django.forms import ModelForm
from .models import Autists, Names
from django import forms



name_list =[('boltz','boltz'),('momvs','momvs'), ('jere','jere'), ('fede','fede'),('czin','czin'),('chefsu','chefsu'),('mots','mots')]


class OpinionForm(ModelForm):
    class Meta:
        model= Autists
        fields = ['name', 'goodOpinion', 'badOpinion']
        labels = {
            "name" : "",
            "goodOpinion": "",
            "badOpinion": ""
        }

        widgets = {
            'name': forms.Select (choices= name_list, attrs= {'class': 'name'}),
            'goodOpinion': forms.Textarea( attrs= {'class': 'good-text' , 'placeholder': 'Deci algo bueno del pibe'}),
            'badOpinion': forms.Textarea( attrs= {'class': 'bad-text' , 'placeholder': 'Aca lo podes bardear'})
            
        }         


