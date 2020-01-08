from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Categoria', max_length=20)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(verbose_name='Categoria', max_length=20)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['name']

    def __str__(self):
        return self.name

class Recomendation(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=200)
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_category')
    state = models.ManyToManyField(State, verbose_name='Estado', related_name='get_state')
    order = models.SmallIntegerField(verbose_name='Posición', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Recomendación'
        verbose_name_plural = 'Recomendaciones'
        ordering = ['-order']

    def __str__(self):
        return self.name