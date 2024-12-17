from django.db import models
from apps.usuario.models import Usuario


class Nucleo(models.Model):
    nome = models.CharField('Nome', max_length=100)
    def __str__(self):
        return self.nome

class Campi(models.Model):
    nome = models.CharField('Nome', max_length=100)
    def __str__(self):
        return self.nome
    
class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)
    def __str__(self):
        return self.nome

class Tipo_Producao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    def __str__(self):
        return self.nome

class Tipo_Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    def __str__(self):
        return self.nome
    
class Projeto(models.Model):
    data_inicio = models.DateField('Data de Início')
    data_fim = models.DateField('Data de Fim')

class Producao(models.Model):
    titulo = models.CharField('Titulo', max_length=150)
    resumo = models.TextField('Resumo')
    imagem = models.ImageField('Imagem', upload_to='producoes', null=True)
    nucleo = models.ForeignKey(Nucleo, on_delete=models.PROTECT)
    tipo_producao = models.ForeignKey(Tipo_Producao, on_delete=models.PROTECT)
    autor_cadastro = models.ForeignKey(Usuario, related_name='producao_autor_cadastro', on_delete=models.PROTECT)
    campi = models.ManyToManyField(Campi)
    projetos = models.ManyToManyField(Projeto)
    pesquisadores = models.ManyToManyField(Usuario)
    areas = models.ManyToManyField(Area)
    def __str__(self):
        return self.titulo
    
class Artigo(models.Model):
    local_producao = models.CharField('Nome', max_length=100)
    producao = models.ForeignKey(Producao, on_delete=models.PROTECT)
    def __str__(self):
        return self.producao.titulo