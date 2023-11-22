from django import forms 
from .models import Productos, Ordenes

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'categoria', 'cantidad']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Ordenes
        fields = ['producto', 'orden_cantidad']