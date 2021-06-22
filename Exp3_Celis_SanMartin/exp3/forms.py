from django import forms 
from django.forms import ModelForm, widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Usuariomoroso, Usuario


class morosoForm(ModelForm): 

    class Meta: 
        model = Usuariomoroso 
        fields = ['idmoroso','nombremoroso','mesesmoroso','usuario']

        labels={
            'idmoroso': 'Digite Id',
            'nombremoroso': 'Digite Nombre', 
            'mesesmoroso': 'Digite Meses de morosidad', 
            'usuario': 'Seleccione Id del usuario'
        }

        widgets={

            'idmoroso': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'idmoroso', 
                    'id': 'idmoroso'
                }
            ),
            'nombremoroso': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'nombremoroso', 
                    'id': 'nombremoroso'
                }
            ),
            'mesesmoroso': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'mesesmoroso', 
                    'id': 'mesesmoroso'
                }
            ), 
            'usuario': forms.Select(    
                attrs={
                    'class': 'form-control', 
                    'id':'usuario'
                }
            ) 
        }