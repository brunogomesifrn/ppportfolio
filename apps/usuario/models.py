from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=100)
    data_nascimento = models.DateField('Data de Nascimento')
    cpf = models.CharField('CPF', max_length=11, unique=True)
    imagem = models.ImageField('Imagem', upload_to='usuarios', null=True)

    USERNAME_FIELD = 'cpf'

