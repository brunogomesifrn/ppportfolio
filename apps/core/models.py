from django.db import models

# Create your models here.


class Nucleo(models.Model):
    nome = models.CharField('Nome', max_length=50)
    def __str__(self):
        return self.nome

class Campi(models.Model):
    nome = models.CharField('Nome', max_length=50)
    def __str__(self):
        return self.nome




'''
class Tipo_Narrativa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    def __str__(self):
        return self.nome

class Estilo_Narrativa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    def __str__(self):
        return self.nome

class Narrativa(models.Model):
    titulo = models.CharField('Titulo', max_length=300)
    descricao = models.TextField('Descricao')
    foto = models.ImageField('Foto', null=True)
    autor = models.CharField('Autor(es)', max_length=200)
    anexo = models.FileField('Anexo', null=True)
    link = models.CharField('Link', null=True, max_length=500)
    tipo_narrativa = models.ForeignKey(Tipo_Narrativa, on_delete=models.PROTECT)
    estilo_narrativa = models.ManyToManyField(Estilo_Narrativa)
    def __str__(self):
        return self.titulo

class Local_Narrativa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    def __str__(self):
        return self.nome

class Turno_Narrativa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    def __str__(self):
        return self.nome

class Periodo_Narrativa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    def __str__(self):
        return self.nome

class Publico_Destino(models.Model):
    nome = models.CharField('Nome', max_length=50)
    def __str__(self):
        return self.nome

class Indicadores_Narrativa(models.Model):
    qtd_personagens_reais = models.IntegerField('Quantidade de Personagens Reais')
    qtd_personagens_imaginarios = models.IntegerField('Quantidade de Personagens Imaginarios')
    qtd_personagens_criancas = models.IntegerField('Quantidade de Personagens Crianças')
    qtd_personagens_adultos = models.IntegerField('Quantidade de Personagens Adultos')
    qtd_personagens_idosos = models.IntegerField('Quantidade de Personagens Idosos')
    qtd_personagens_animais = models.IntegerField('Quantidade de Personagens Animais')
    narrativa = models.ForeignKey(Narrativa, on_delete=models.PROTECT)
    locais = models.ManyToManyField(Local_Narrativa)
    turnos = models.ManyToManyField(Turno_Narrativa)
    publicos = models.ManyToManyField(Publico_Destino)
    periodo = models.ForeignKey(Periodo_Narrativa, on_delete=models.PROTECT)
    def __str__(self):
        return "Indicadores da Narrativa: ",self.narrativa.titulo


'''