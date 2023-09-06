from django import forms

class cursoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()
    