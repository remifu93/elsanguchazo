from django.db import models
from category.models import Category


class Option(models.Model):

    name = models.CharField('Nombre', max_length=100)
    name_en = models.CharField('Name', max_length=100, blank=True, null=True)
    description = models.TextField('Descripcion', blank=True, null=True)
    description_en = models.TextField('Description', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    price = models.IntegerField('Precio', default=0)
    recommended = models.BooleanField('Recomendado', default=False)
    
    class Meta:
        verbose_name = "Comida"
        verbose_name_plural = "Comidas"

    def __str__(self):
        return self.name