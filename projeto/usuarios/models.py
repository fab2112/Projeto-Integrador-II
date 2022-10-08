# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    Primeironome = models.CharField(max_length=20, null=True, blank=False, verbose_name='Primeiro Nome')
    Segundonome = models.CharField(max_length=20, null=True, blank=False, verbose_name='Segundo Nome')
    Tel = models.CharField(max_length=15, null=True, blank=True, verbose_name='Tel')
    cpf = models.CharField(max_length=15, null=True, blank=True, verbose_name='CPF/CNPJ')
