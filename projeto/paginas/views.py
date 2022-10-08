# paginas/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class sobrenosView(TemplateView):
    template_name = 'sobrenos.html'

