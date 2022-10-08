# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username',
            'Primeironome',
            'Segundonome',
            'email',
            'Tel',
            'cpf',
        )
        help_texts = {
            'username': '(Obrigatório)',
            'Primeironome': '(Obrigatório)',
            'Segundonome': '(Obrigatório)',
            'email': '(Obrigatório)',
            'Tel': '(Opcional)',
            'cpf': '(Opcional)'
        }
        blank = {
            'email': False
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'Primeironome',
            'Segundonome',
            'email',
            'Tel',
            'cpf',
        )
