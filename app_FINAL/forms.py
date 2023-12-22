from django import forms
from django.forms import ModelForm

from app_FINAL.models import Inscritos, Instituciones

class Instituciones_Form(ModelForm):
    class Meta:
        model = Instituciones
        fields = '__all__'
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Inscritos_Form(ModelForm):
    class Meta:
        model = Inscritos
        fields = ['nombre', 'telefono', 'institucion', 'estado', 'observacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'institucion': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'}),
        }