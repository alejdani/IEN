from socket import fromshare
from django import forms 
from .models import Articulo


class FormularioArticulos(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.FloatField()
    descripcion= forms.CharField(required=False)
class FormularioArticle(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ["nombre"]