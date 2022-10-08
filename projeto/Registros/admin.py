# Registros/admin.py
from django.contrib import admin
from .models import Registro, Comentario, Recebido
from django.contrib.admin.models import LogEntry


class ComentarioInline(admin.TabularInline):
    model = Comentario


class RecebidoInline(admin.TabularInline):
    model = Recebido


class RegistroAdmin(admin.ModelAdmin):
    inlines = [ComentarioInline, RecebidoInline]


# LogEntry.objects.all().delete()

admin.site.register(Registro, RegistroAdmin)
admin.site.register(Comentario)
admin.site.register(Recebido)
