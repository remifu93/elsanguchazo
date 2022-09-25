from pyexpat import model
from django.db import models


class Category(models.Model):
    name = models.CharField('Nombre', max_length=50)
    image = models.ImageField('Imagen', upload_to='category', blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name