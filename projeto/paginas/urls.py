# paginas/urls.py
from django.urls import path
from .views import HomePageView, sobrenosView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('sobrenos', sobrenosView.as_view(), name='sobrenos'),
]

