from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def parcerias(request):
    return render(request, 'parcerias.html')

def contato(request):
    return render(request, 'contato.html')

def detalhes_nucleo(request):
    return render(request, 'detalhes_nucleo.html')

def login(request):
    return render(request, 'login.html')

def nucleo_acao(request):
    return render(request, 'nucleo_acao.html')

def pagina_acoes(request):
    return render(request, 'pagina_acoes.html')

def registro(request):
    return render(request, 'registro.html')

def sobre(request):
    return render(request, 'sobre.html')
