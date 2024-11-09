from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    apelido = forms.CharField(max_length=50, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'apelido', 'password1', 'password2']