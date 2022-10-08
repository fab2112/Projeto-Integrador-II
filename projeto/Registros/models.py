# Registros/models.py
from django.conf import settings
from django.contrib.auth import get_user_model, get_user
from django.db import models
from django.urls import reverse
from usuarios.models import CustomUser
from django.utils.functional import lazy
from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=30)
    new_image = File(im_io, name=image.name)
    return new_image


class Registro(models.Model):
    doacao = models.CharField(max_length=255, verbose_name='Doação')
    contato = models.CharField(max_length=255, null=True, blank=False, verbose_name='Telefone para contato')
    endereco = models.CharField(max_length=255, null=True, blank=False, verbose_name='Endereço para entrega')
    obs = models.TextField(blank=True, verbose_name='Observação')
    data_1 = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    doador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
    status = models.BooleanField(default=True)
    image = models.ImageField(verbose_name='Upload imagem')

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.doacao

    def get_absolute_url(self):
        return reverse('registro_list')


class Comentario(models.Model):
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, related_name='comentarios', )
    comentario = models.CharField(max_length=500, blank=False, verbose_name='Menssagem')
    data_2 = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data')
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('registro_list')


class Recebido(models.Model):
    recebido = models.ForeignKey(Registro, on_delete=models.CASCADE, related_name='registro_rec', )
    data_3 = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data')
    contato_2 = models.CharField(max_length=500, blank=False, null=True, verbose_name='Confirmar tel.:')
    receptor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False, related_name='receptor')

    def __str__(self):
        return str(self.recebido)

    def get_absolute_url(self):
        return reverse('registro_list')

