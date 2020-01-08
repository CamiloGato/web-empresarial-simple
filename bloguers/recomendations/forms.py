from django import forms
from .models import Recomendation, Category

class RecomendationForm(forms.ModelForm):
    
    class Meta:
        model = Recomendation
        fields= ['name', 'categories', 'state','order']
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Titulo',
                }),
            'categories': forms.SelectMultiple(attrs={
                'class':'form-control',
                }),
            'state': forms.SelectMultiple(attrs={
                'class':'form-control',
                }),
            'order': forms.NumberInput(attrs={
                'class':'form-control',
                }),
        }
        labels = {
            'name': 'Recomendación',
            'categories': 'Seleccionar Categorias (Con Control presionado puede escoger varias)',
            'order': 'Orden (Mas grandes primero)',
        }

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields= ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombre Categoría'
                }),
        }
        labels = {
            'name': 'Nombre de la categoría',
        }