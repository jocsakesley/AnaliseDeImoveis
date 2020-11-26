from django.urls import path, include
from analise_de_imoveis.core.views import index

urlpatterns = [
    path('', index, name='index')
]