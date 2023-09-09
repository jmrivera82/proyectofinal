from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registrousuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        help_texts = {k:"" for k in fields}
