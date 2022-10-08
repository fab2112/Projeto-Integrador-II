# Projeto_core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('Registros/', include('Registros.urls')),
    path('', include('paginas.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)