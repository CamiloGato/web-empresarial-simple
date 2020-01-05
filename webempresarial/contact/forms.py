from django import forms

# Formulario de contacto
class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Escribe tu nombre aquí'}
    ))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder': 'Escribe tu email aquí'}
    ))
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder': 'Escribe tu mensaje aquí'}
    ))