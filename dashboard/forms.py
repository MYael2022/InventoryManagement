from django import forms 
from .models import Productos

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'categoria', 'cantidad']