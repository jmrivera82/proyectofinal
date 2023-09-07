from django import forms

class cursoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()
    
class profesorForm(forms.Form):
        nombre=forms.CharField(max_length=50)
        apellido=forms.CharField(max_length=50)
        email=forms.EmailField()
        profesion=forms.CharField(max_length=50)


    