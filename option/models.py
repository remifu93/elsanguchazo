from django.db import models
from category.models import Category


class Option(models.Model):

    name = models.CharField('Nombre', max_length=30)
    description = models.TextField('Descripcion', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    price = models.IntegerField('Precio', default=0)
    recommended = models.BooleanField('Recomendado', default=False)
    
    class Meta:
        verbose_name = "Comida"
        verbose_name_plural = "Comidas"

    def __str__(self):
        return self.name