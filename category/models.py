from pyexpat import model
from django.db import models


class Category(models.Model):
    name = models.CharField('Nombre', max_length=100)
    name_en = models.CharField('Name', max_length=100, blank=True, null=True)
    image = models.ImageField('Imagen', upload_to='category', blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f'{self.name} - {self.name_en}'