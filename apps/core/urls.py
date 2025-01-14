from django.urls import path
from .views import index, parcerias, contato, detalhes_nucleo, login, nucleo_acao, pagina_acoes, registro, sobre

urlpatterns = [
    path('', index, name='index'),
    path('parcerias/', parcerias, name='parcerias'),
    path('contato/', contato, name='contato'),
    path('detalhes_nucleo/', detalhes_nucleo, name='detalhes_nucleo'),
    path('login/', login, name='login'),
    path('nucleo_acao/', nucleo_acao, name='nucleo_acao'),
    path('pagina_acoes/', pagina_acoes, name='pagina_acoes'),
    path('registro/', registro, name='registro'),
    path('sobre/', sobre, name='sobre'),
]
