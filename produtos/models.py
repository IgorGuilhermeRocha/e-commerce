from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Produto(models.Model):

    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    imagem = models.ImageField(upload_to='produto_images/%Y/%m',blank=True,null=True)
    slug =  models.SlugField(unique=True)
    preco_original = models.FloatField(default=0)
    preco_promo = models.FloatField()
    tam = models.CharField(
        max_length=255,
        choices= (
            ('P','pequena'),
            ('M','média'),
            ('G','grande'),
        )
    )