from distutils.command.upload import upload
from turtle import width
from django.db import models
from PIL import Image
import os
from django.conf import settings

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

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        if original_width <= new_width:
            print("largura original menor que nova largura")
            img_pil.close
            return
        new_height = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height),Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize = True,
            quality=50
        )

      

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if(self.imagem):
            self.resize_image(self.imagem, max_image_size)


    def __str__ (self):
        return self.nome